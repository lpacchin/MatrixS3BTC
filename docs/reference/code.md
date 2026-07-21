# Reference: code

> SHA: `b40b9be` · Copertura LLM: 7/7  
> Fotografia generata da `funcref.generate` — overview ACTIVE-only, storico completo nel corpo.

## Module Overview

Il modulo `code` possiede **7** funzioni ACTIVE, di cui **0** endpoint HTTP.  
Dipende da (chiamate uscenti cross-module): nessun modulo interno.  
È usato da (chiamate entranti cross-module): nessun modulo interno.

| Funzione | Firma | Route | Scopo |
|---|---|---|---|
| [`code.animate_price_change`](#code.animate_price_change) | `animate_price_change(old_price, new_price, color)` | `—` | Mostra un'animazione progressiva sul display della matrice che trasforma una stringa di prezzo da vecchio a nuovo colore, simulando un cambio di cifra passo-passo. |
| [`code.connect_wifi`](#code.connect_wifi) | `connect_wifi()` | `—` | Tenta la connessione WiFi con SSID e password globali, entro un timeout di 20 secondi, restituendo esito booleano. |
| [`code.darker`](#code.darker) | `darker(color, factor=0.2)` | `—` | Scurisce un colore RGB moltiplicando ciascun componente R, G, B per un fattore riduttivo, restituendo il nuovo colore impacchettato. |
| [`code.format_high_low`](#code.format_high_low) | `format_high_low(value)` | `—` | Formatta un valore numerico in una stringa con il simbolo del dollaro, convertendolo in intero. |
| [`code.format_price`](#code.format_price) | `format_price(value)` | `—` | Converte un valore in intero e lo formatta con separatore delle migliaia apostrofo e suffisso dollaro, utile per visualizzare prezzi arrotondati. |
| [`code.pad_left`](#code.pad_left) | `pad_left(text, width)` | `—` | Assicura che una stringa abbia una lunghezza minima, aggiungendo spazi a sinistra se necessario. |
| [`code.reset_wifi`](#code.reset_wifi) | `reset_wifi()` | `—` | Resetta la connessione WiFi disabilitando e riabilitando la radio, poi tenta la riconnessione tramite la funzione connect_wifi(). |

---

<!-- fn:code.animate_price_change -->
## `code.animate_price_change` <a name="code.animate_price_change"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `animate_price_change(old_price, new_price, color)`  
**Async**: no  
**Posizione**: `code.py:194`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.pad_left`](#code.pad_left), [`code.py.old.pad_left`](#code.py.old.pad_left), [`code.py.old1.pad_left`](#code.py.old1.pad_left)  
**Chiamata da**: —  

**Scopo**: Mostra un'animazione progressiva sul display della matrice che trasforma una stringa di prezzo da vecchio a nuovo colore, simulando un cambio di cifra passo-passo.

**Input**: old_price: str o None (convertito a '' se None); new_price: str (nuovo prezzo); color: valore colore accettato da matrixportal.set_text_color.

**Output**: Nessun valore di ritorno (None). Modifica direttamente il display via matrixportal e dorme per la durata.

**Gotcha**: La funzione dipende da variabili globali `matrixportal` e `price_index`, non definite al suo interno.

<!-- fn:code.connect_wifi -->
## `code.connect_wifi` <a name="code.connect_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `connect_wifi()`  
**Async**: no  
**Posizione**: `code.py:24`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.py.old.reset_wifi`](#code.py.old.reset_wifi), [`code.py.old1.reset_wifi`](#code.py.old1.reset_wifi), [`code.reset_wifi`](#code.reset_wifi)  

**Scopo**: Tenta la connessione WiFi con SSID e password globali, entro un timeout di 20 secondi, restituendo esito booleano.

**Input**: nessun parametro

**Output**: True se la connessione è riuscita, False in caso di timeout o errore durante il tentativo.

**Gotcha**: Dipende dalle variabili globali WIFI_SSID, WIFI_PASSWORD e dal modulo wifi; blocca l'esecuzione per l'intero timeout.

<!-- fn:code.darker -->
## `code.darker` <a name="code.darker"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `darker(color, factor=0.2)`  
**Async**: no  
**Posizione**: `code.py:57`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.py.old1.set_display_state`](#code.py.old1.set_display_state)  

**Scopo**: Scurisce un colore RGB moltiplicando ciascun componente R, G, B per un fattore riduttivo, restituendo il nuovo colore impacchettato.

**Input**: color: intero non negativo che rappresenta un colore a 24-bit (8 bit per canale); factor: float, tipicamente in [0,1] per scurire

**Output**: nuovo intero a 24-bit con i canali scalati e troncati (stessa modalità di impacchettamento)

**Gotcha**: Il troncamento intero dopo la moltiplicazione può causare perdita di precisione; se factor > 1 i valori dei canali superano 255 e l'assemblaggio finale può generare componenti spurie oltre i 24 bit, producendo un risultato imprevedibile.

<!-- fn:code.format_high_low -->
## `code.format_high_low` <a name="code.format_high_low"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_high_low(value)`  
**Async**: no  
**Posizione**: `code.py:185`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Formatta un valore numerico in una stringa con il simbolo del dollaro, convertendolo in intero.

**Input**: value: qualsiasi tipo convertibile a int (es. int, float, stringa numerica).

**Output**: Restituisce una stringa nel formato '<intero> $'. Lancia ValueError o TypeError se la conversione a int fallisce.

**Gotcha**: La conversione a int tronca la parte decimale senza arrotondamento. La stringa restituita contiene uno spazio prima di '$'.

<!-- fn:code.format_price -->
## `code.format_price` <a name="code.format_price"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_price(value)`  
**Async**: no  
**Posizione**: `code.py:180`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Converte un valore in intero e lo formatta con separatore delle migliaia apostrofo e suffisso dollaro, utile per visualizzare prezzi arrotondati.

**Input**: value: qualsiasi input convertibile a int (es. stringa numerica, int, float senza parte decimale).

**Output**: Stringa nel formato `1'234$`. Può sollevare ValueError se la conversione a int fallisce.

**Gotcha**: La formattazione sostituisce le virgole con apostrofi; non adatta il separatore alla localizzazione dell'utente.

<!-- fn:code.pad_left -->
## `code.pad_left` <a name="code.pad_left"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `pad_left(text, width)`  
**Async**: no  
**Posizione**: `code.py:189`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.animate_price_change`](#code.animate_price_change), [`code.py.old.animate_price_change`](#code.py.old.animate_price_change), [`code.py.old1.animate_price_change`](#code.py.old1.animate_price_change)  

**Scopo**: Assicura che una stringa abbia una lunghezza minima, aggiungendo spazi a sinistra se necessario.

**Input**: text: str (qualsiasi stringa); width: int (lunghezza minima desiderata).

**Output**: str: il testo originale se len(text) >= width, altrimenti una nuova stringa con spazi anteposti per raggiungere width.

**Gotcha**: —

<!-- fn:code.reset_wifi -->
## `code.reset_wifi` <a name="code.reset_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `reset_wifi()`  
**Async**: no  
**Posizione**: `code.py:43`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.connect_wifi`](#code.connect_wifi), [`code.py.old.connect_wifi`](#code.py.old.connect_wifi), [`code.py.old1.connect_wifi`](#code.py.old1.connect_wifi)  
**Chiamata da**: —  

**Scopo**: Resetta la connessione WiFi disabilitando e riabilitando la radio, poi tenta la riconnessione tramite la funzione connect_wifi().

**Input**: Nessun parametro.

**Output**: Ritorna il valore restituito da connect_wifi() (presumibilmente un booleano) oppure False in caso di eccezione durante il reset.

**Gotcha**: —
