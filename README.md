# MatrixS3BTC

Firmware CircuitPython per Adafruit MatrixPortal S3 con pannello LED HUB75 64x32 - Display del prezzo Bitcoin in tempo reale.

## Descrizione

Visualizza il prezzo corrente di Bitcoin su un pannello LED RGB 64x32 pilotato da un MatrixPortal S3. Il prezzo viene aggiornato periodicamente da API Bybit con indicazione visiva delle variazioni tramite colori (verde = rialzo, rosso = ribasso). Include un mini server HTTP integrato per controllo remoto.

## Funzionalita

- **Prezzo BTC in tempo reale** da API Bybit
- **Indicazione variazione** con flash verde (rialzo) e rosso (ribasso)
- **High/Low 24h** visualizzati sul display
- **Dark mode** notturna con fattore di attenuazione configurabile (NORMAL_FACTOR / NIGHT_FACTOR)
- **Server HTTP integrato** con interfaccia web per accendere/spegnere il display da remoto
- **Gestione Wi-Fi** robusta con riconnessione automatica e reset
- **Font personalizzato** FiraSans-Bold-14 per massima leggibilita

## Stack Tecnologico

- **Microcontrollore**: Adafruit MatrixPortal S3 (ESP32-S3)
- **Display**: Pannello LED RGB HUB75 64x32
- **Linguaggio**: CircuitPython
- **Librerie**: adafruit_matrixportal, adafruit_requests, adafruit_ntp, adafruit_httpserver, adafruit_bitmap_font

## Configurazione

Credenziali Wi-Fi nel file `settings.toml`.

## Struttura File

| File/Cartella | Descrizione |
|---------------|-------------|
| `code.py` | Firmware principale |
| `code.py.old.py` | Versione precedente (backup) |
| `code.py.old1.py` | Versione precedente (backup) |
| `fonts/` | Font BDF per il display (FiraSans-Bold-14) |
| `lib/` | Librerie CircuitPython |
| `sd/` | File su SD card |
| `settings.toml` | Configurazione Wi-Fi e parametri |
