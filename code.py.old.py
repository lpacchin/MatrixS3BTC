import time
import wifi
import board
import socketpool
import ssl
import adafruit_requests
from adafruit_matrixportal.matrixportal import MatrixPortal
import adafruit_bitmap_font.bitmap_font as bitmap_font
import terminalio
import os
import microcontroller  # Per resettare il dispositivo in caso estremo

# -----------------------------
# Impostazioni WiFi
# -----------------------------
WIFI_SSID = "lupa"
WIFI_PASSWORD = "780130bmw."

# -----------------------------
# Funzione per connettere o riconnettere il WiFi
# -----------------------------
def connect_wifi():
    print("Tentativo di connessione WiFi a '{}'...".format(WIFI_SSID))
    timeout = 20
    start_time = time.monotonic()
    wifi.radio.enabled = True  # Assicura che il radio sia attivo
    while time.monotonic() - start_time < timeout:
        try:
            wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
            print("Connesso! Indirizzo IP:", wifi.radio.ipv4_address)
            return True
        except Exception as e:
            print("Errore nella connessione WiFi:", e)
            time.sleep(1)
    print("Timeout connessione WiFi")
    return False

# -----------------------------
# Funzione per resettare il WiFi
# -----------------------------
def reset_wifi():
    print("Reset della connessione WiFi...")
    try:
        wifi.radio.enabled = False  # Disabilita il radio
        time.sleep(1)  # Breve attesa
        wifi.radio.enabled = True  # Riabilita il radio
        return connect_wifi()  # Tenta la riconnessione
    except Exception as e:
        print("Errore durante il reset WiFi:", e)
        return False

# -----------------------------
# Debug: Elenca i file in /fonts/
# -----------------------------
print("Contenuto di /fonts/:")
try:
    font_files = os.listdir("/fonts")
    print(font_files)
except Exception as e:
    print("Errore nell'accesso a /fonts/:", e)
    font_files = []

# -----------------------------
# Verifica il font personalizzato per il prezzo
# -----------------------------
font_path = "/fonts/FiraSans-Bold-14.bdf"
font_filename = font_path.split("/")[-1]
if font_filename in font_files:
    print("Font trovato:", font_path)
    DISPLAY_FONT_PRICE = font_path  # Percorso per il prezzo
else:
    print("Font non trovato, uso fallback per il prezzo")
    DISPLAY_FONT_PRICE = terminalio.FONT

# Font per massimo e minimo
DISPLAY_FONT_HIGH_LOW = terminalio.FONT

# -----------------------------
# Inizializza il display Matrix 64x32
# -----------------------------
matrixportal = MatrixPortal(
    width=64,
    height=32,
    bit_depth=6,
    debug=False
)

# -----------------------------
# Creazione dei campi di testo
# -----------------------------
price_index = matrixportal.add_text(
    text_font=DISPLAY_FONT_PRICE,
    text_position=(10, 7),
    scrolling=False,
    text_scale=0.5
)

high_index = matrixportal.add_text(
    text_font=DISPLAY_FONT_HIGH_LOW,
    text_position=(2, 4),
    scrolling=False,
    text_scale=0.5
)

low_index = matrixportal.add_text(
    text_font=DISPLAY_FONT_HIGH_LOW,
    text_position=(2, 27),
    scrolling=False,
    text_scale=0.5
)

# -----------------------------
# Testo di startup
# -----------------------------
matrixportal.set_text("BTC-USD", index=price_index)
matrixportal.set_text_color(0x00FF00, index=price_index)
time.sleep(2)

# -----------------------------
# Connessione WiFi iniziale
# -----------------------------
if not connect_wifi():
    matrixportal.set_text("WiFi Error", index=price_index)
    matrixportal.set_text_color(0xFF0000, index=price_index)
    while True:
        time.sleep(1)

# -----------------------------
# Inizializzazione HTTP
# -----------------------------
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()
requests = adafruit_requests.Session(pool, ssl_context)

BYBIT_URL = "https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT"

# -----------------------------
# Variabili globali
# -----------------------------
last_update_time = 0
update_interval = 6
last_price = None
last_high = None
last_low = None
previous_price_value = None
default_color = 0xa36c00  # Arancione per prezzo invariato
up_color = 0x006400       # Verde scuro per prezzo in salita
down_color = 0x8B0000     # Rosso scuro per prezzo in discesa
high_color = 0x006400     # Verde scuro per massimo
low_color = 0x8B0000      # Rosso scuro per minimo
failed_attempts = 0
max_failed_attempts = 3
max_reset_attempts = 3    # Numero massimo di reset WiFi prima di un hard reset

# Funzioni di formattazione e animazione
def format_price(value):
    value = int(value)
    formatted = f"{value:,}".replace(",", "'")
    return f"{formatted} $"

def format_high_low(value):
    value = int(value)
    return f"{value} $"

def pad_left(text, width):
    if len(text) >= width:
        return text
    return " " * (width - len(text)) + text

def animate_price_change(old_price, new_price, color):
    if old_price is None:
        old_price = ""
    max_len = max(len(old_price), len(new_price))
    old_price = pad_left(old_price, max_len)
    new_price = pad_left(new_price, max_len)

    animation_duration = 1.0
    steps = 10
    step_duration = animation_duration / steps

    for step in range(steps):
        current_text = list(new_price)
        for i in range(max_len):
            if old_price[i] != new_price[i] and new_price[i].isdigit():
                current_digit = (step % 10)
                if current_digit <= int(new_price[i]) or step == steps - 1:
                    current_text[i] = new_price[i]
                else:
                    current_text[i] = str(current_digit)
        matrixportal.set_text("".join(current_text), index=price_index)
        matrixportal.set_text_color(color, index=price_index)
        time.sleep(step_duration)

    matrixportal.set_text(new_price, index=price_index)
    matrixportal.set_text_color(color, index=price_index)

# -----------------------------
# Loop principale
# -----------------------------
reset_attempts = 0
print("Usando URL:", BYBIT_URL)
while True:
    current_time = time.monotonic()

    if current_time - last_update_time >= update_interval:
        try:
            response = requests.get(BYBIT_URL, timeout=5)
            print("Codice HTTP:", response.status_code)

            if response.status_code != 200:
                print("Errore HTTP:", response.status_code, response.text)
                failed_attempts += 1
                if failed_attempts >= max_failed_attempts:
                    matrixportal.set_text("Conn Error", index=price_index)
                    matrixportal.set_text_color(0xFF0000, index=price_index)
                    # Tenta il reset WiFi
                    if reset_attempts < max_reset_attempts:
                        if reset_wifi():
                            # Reinizializza HTTP
                            pool = socketpool.SocketPool(wifi.radio)
                            ssl_context = ssl.create_default_context()
                            requests = adafruit_requests.Session(pool, ssl_context)
                            failed_attempts = 0
                            reset_attempts += 1
                            matrixportal.set_text(last_price or "BTC-USD", index=price_index)
                            matrixportal.set_text_color(default_color, index=price_index)
                        else:
                            print("Reset WiFi fallito")
                            reset_attempts += 1
                    else:
                        print("Massimo numero di reset raggiunto, riavvio dispositivo")
                        microcontroller.reset()  # Hard reset
                response.close()
                continue

            try:
                data = response.json()
            except ValueError as e:
                print("Errore JSON:", str(e))
                print("Risposta grezza:", response.text)
                failed_attempts += 1
                if failed_attempts >= max_failed_attempts:
                    matrixportal.set_text("JSON Error", index=price_index)
                    matrixportal.set_text_color(0xFF0000, index=price_index)
                    # Tenta il reset WiFi
                    if reset_attempts < max_reset_attempts:
                        if reset_wifi():
                            pool = socketpool.SocketPool(wifi.radio)
                            ssl_context = ssl.create_default_context()
                            requests = adafruit_requests.Session(pool, ssl_context)
                            failed_attempts = 0
                            reset_attempts += 1
                            matrixportal.set_text(last_price or "BTC-USD", index=price_index)
                            matrixportal.set_text_color(default_color, index=price_index)
                        else:
                            print("Reset WiFi fallito")
                            reset_attempts += 1
                    else:
                        print("Massimo numero di reset raggiunto, riavvio dispositivo")
                        microcontroller.reset()
                response.close()
                continue

            if data["retCode"] == 0:
                ticker = data["result"]["list"][0]
                price = float(ticker["lastPrice"])
                high = float(ticker["highPrice24h"])
                low = float(ticker["lowPrice24h"])

                price_text = format_price(price)
                high_text = f"H:{format_high_low(high)}"
                low_text = f"L:{format_high_low(low)}"

                if previous_price_value is None:
                    price_color = default_color
                elif price > previous_price_value:
                    price_color = up_color
                elif price < previous_price_value:
                    price_color = down_color
                else:
                    price_color = default_color

                if price_text != last_price:
                    animate_price_change(last_price, price_text, color=price_color)
                    last_price = price_text
                elif last_price is None:
                    matrixportal.set_text(price_text, index=price_index)
                    matrixportal.set_text_color(price_color, index=price_index)
                    last_price = price_text

                if high_text != last_high:
                    matrixportal.set_text(high_text, index=high_index)
                    matrixportal.set_text_color(high_color, index=high_index)
                    last_high = high_text

                if low_text != last_low:
                    matrixportal.set_text(low_text, index=low_index)
                    matrixportal.set_text_color(low_color, index=low_index)
                    last_low = low_text

                previous_price_value = price
                failed_attempts = 0
                reset_attempts = 0  # Resetta i tentativi di reset dopo un successo
                last_update_time = current_time
            else:
                print("Errore API Bybit:", data["retMsg"])
                failed_attempts += 1
                if failed_attempts >= max_failed_attempts:
                    matrixportal.set_text("API Error", index=price_index)
                    matrixportal.set_text_color(0xFF0000, index=price_index)
                    # Tenta il reset WiFi
                    if reset_attempts < max_reset_attempts:
                        if reset_wifi():
                            pool = socketpool.SocketPool(wifi.radio)
                            ssl_context = ssl.create_default_context()
                            requests = adafruit_requests.Session(pool, ssl_context)
                            failed_attempts = 0
                            reset_attempts += 1
                            matrixportal.set_text(last_price or "BTC-USD", index=price_index)
                            matrixportal.set_text_color(default_color, index=price_index)
                        else:
                            print("Reset WiFi fallito")
                            reset_attempts += 1
                    else:
                        print("Massimo numero di reset raggiunto, riavvio dispositivo")
                        microcontroller.reset()

            response.close()

        except Exception as e:
            print("Errore nella richiesta:", str(e))
            failed_attempts += 1
            if failed_attempts >= max_failed_attempts:
                matrixportal.set_text("Conn Error", index=price_index)
                matrixportal.set_text_color(0xFF0000, index=price_index)
                # Tenta il reset WiFi
                if reset_attempts < max_reset_attempts:
                    if reset_wifi():
                        pool = socketpool.SocketPool(wifi.radio)
                        ssl_context = ssl.create_default_context()
                        requests = adafruit_requests.Session(pool, ssl_context)
                        failed_attempts = 0
                        reset_attempts += 1
                        matrixportal.set_text(last_price or "BTC-USD", index=price_index)
                        matrixportal.set_text_color(default_color, index=price_index)
                    else:
                        print("Reset WiFi fallito")
                        reset_attempts += 1
                else:
                    print("Massimo numero di reset raggiunto, riavvio dispositivo")
                    microcontroller.reset()

    time.sleep(0.1)
