# Reference: code.py.old

> SHA: `b40b9be` · Copertura LLM: 6/6  
> Fotografia generata da `funcref.generate` — overview ACTIVE-only, storico completo nel corpo.

## Module Overview

Il modulo `code.py.old` possiede **6** funzioni ACTIVE, di cui **0** endpoint HTTP.  
Dipende da (chiamate uscenti cross-module): `code`.  
È usato da (chiamate entranti cross-module): `code`.

| Funzione | Firma | Route | Scopo |
|---|---|---|---|
| [`code.py.old.animate_price_change`](#code.py.old.animate_price_change) | `animate_price_change(old_price, new_price, color)` | `—` | Anima il passaggio da old_price a new_price su un display matrixportal, mostrando una sequenza di cifre che scorrono per un effetto di aggiornamento graduale. |
| [`code.py.old.connect_wifi`](#code.py.old.connect_wifi) | `connect_wifi()` | `—` | Tenta di connettersi a una rete WiFi con SSID e password globali, ritentando fino a 20 secondi. Restituisce True se connesso, False altrimenti. |
| [`code.py.old.format_high_low`](#code.py.old.format_high_low) | `format_high_low(value)` | `—` | Formatta un valore numerico in una stringa con suffisso '$' per la visualizzazione (es. prezzi). |
| [`code.py.old.format_price`](#code.py.old.format_price) | `format_price(value)` | `—` | Formatta un prezzo come intero con separatore di migliaia (apostrofo) e simbolo $ finale |
| [`code.py.old.pad_left`](#code.py.old.pad_left) | `pad_left(text, width)` | `—` | Allinea a destra una stringa aggiungendo spazi a sinistra fino alla larghezza specificata. |
| [`code.py.old.reset_wifi`](#code.py.old.reset_wifi) | `reset_wifi()` | `—` | Ripristina la connessione WiFi disabilitando e riabilitando il modulo radio e richiamando connect_wifi() per riconnettersi. |

---

<!-- fn:code.py.old.animate_price_change -->
## `code.py.old.animate_price_change` <a name="code.py.old.animate_price_change"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `animate_price_change(old_price, new_price, color)`  
**Async**: no  
**Posizione**: `code.py.old.py:170`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.pad_left`](#code.pad_left), [`code.py.old.pad_left`](#code.py.old.pad_left), [`code.py.old1.pad_left`](#code.py.old1.pad_left)  
**Chiamata da**: —  

**Scopo**: Anima il passaggio da old_price a new_price su un display matrixportal, mostrando una sequenza di cifre che scorrono per un effetto di aggiornamento graduale.

**Input**: old_price: str o None (None diventa ''); new_price: str (es. '1234'); color: accettato da matrixportal.set_text_color. Entrambi i prezzi vengono allineati con padding a sinistra in base alla lunghezza massima.

**Output**: Nessun valore di ritorno (None). L'animazione viene eseguita a blocchi; eventuali eccezioni propagano da pad_left o da metodi di matrixportal.

**Gotcha**: La funzione richiede la presenza di variabili globali matrixportal (oggetto display) e price_index (indice) precedentemente impostate. Il padding sinistro usa pad_left esterno; caratteri non numerici in new_price non partecipano all'animazione. Il parametro old_price può essere None, gestito come stringa vuota.

<!-- fn:code.py.old.connect_wifi -->
## `code.py.old.connect_wifi` <a name="code.py.old.connect_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `connect_wifi()`  
**Async**: no  
**Posizione**: `code.py.old.py:22`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.py.old.reset_wifi`](#code.py.old.reset_wifi), [`code.py.old1.reset_wifi`](#code.py.old1.reset_wifi), [`code.reset_wifi`](#code.reset_wifi)  

**Scopo**: Tenta di connettersi a una rete WiFi con SSID e password globali, ritentando fino a 20 secondi. Restituisce True se connesso, False altrimenti.

**Input**: nessun parametro

**Output**: True in caso di connessione riuscita, False se si esaurisce il timeout. Le eccezioni di connessione sono catturate e stampate, non propagate.

**Gotcha**: Utilizza variabili globali WIFI_SSID e WIFI_PASSWORD non passate come parametri; modifica wifi.radio.enabled come side-effect; stampa su stdout; non solleva eccezioni.

<!-- fn:code.py.old.format_high_low -->
## `code.py.old.format_high_low` <a name="code.py.old.format_high_low"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_high_low(value)`  
**Async**: no  
**Posizione**: `code.py.old.py:161`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Formatta un valore numerico in una stringa con suffisso '$' per la visualizzazione (es. prezzi).

**Input**: value: qualsiasi valore convertibile a int tramite int() (stringa di cifre, intero, float che verrà troncato).

**Output**: Restituisce una stringa nella forma '<intero> $'. Solleva ValueError se value non è convertibile a int.

**Gotcha**: La conversione int() tronca verso zero, quindi 2.9 -> '2 $'.

<!-- fn:code.py.old.format_price -->
## `code.py.old.format_price` <a name="code.py.old.format_price"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_price(value)`  
**Async**: no  
**Posizione**: `code.py.old.py:156`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Formatta un prezzo come intero con separatore di migliaia (apostrofo) e simbolo $ finale

**Input**: value: numero o stringa convertibile a int (es. 1234, "1234")

**Output**: Restituisce una stringa formattata (es. "1'234 $"). Solleva ValueError se value non è convertibile a int.

**Gotcha**: La conversione a int tronca i decimali senza arrotondamento. Se value è non convertibile, solleva ValueError.

<!-- fn:code.py.old.pad_left -->
## `code.py.old.pad_left` <a name="code.py.old.pad_left"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `pad_left(text, width)`  
**Async**: no  
**Posizione**: `code.py.old.py:165`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.animate_price_change`](#code.animate_price_change), [`code.py.old.animate_price_change`](#code.py.old.animate_price_change), [`code.py.old1.animate_price_change`](#code.py.old1.animate_price_change)  

**Scopo**: Allinea a destra una stringa aggiungendo spazi a sinistra fino alla larghezza specificata.

**Input**: text: stringa; width: intero (lunghezza finale desiderata)

**Output**: Stringa: text se len(text) >= width, altrimenti text preceduta da spazi per raggiungere width.

**Gotcha**: —

<!-- fn:code.py.old.reset_wifi -->
## `code.py.old.reset_wifi` <a name="code.py.old.reset_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `reset_wifi()`  
**Async**: no  
**Posizione**: `code.py.old.py:41`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.connect_wifi`](#code.connect_wifi), [`code.py.old.connect_wifi`](#code.py.old.connect_wifi), [`code.py.old1.connect_wifi`](#code.py.old1.connect_wifi)  
**Chiamata da**: —  

**Scopo**: Ripristina la connessione WiFi disabilitando e riabilitando il modulo radio e richiamando connect_wifi() per riconnettersi.

**Input**: nessun parametro

**Output**: Restituisce il risultato di connect_wifi() (tipicamente un booleano); in caso di eccezione restituisce False.

**Gotcha**: Richiede che wifi.radio e connect_wifi siano accessibili nello scope; eventuali errori sono catturati e restituiti come False senza indicazione del problema.
