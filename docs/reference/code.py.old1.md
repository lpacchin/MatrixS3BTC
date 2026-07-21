# Reference: code.py.old1

> SHA: `b40b9be` · Copertura LLM: 10/10  
> Fotografia generata da `funcref.generate` — overview ACTIVE-only, storico completo nel corpo.

## Module Overview

Il modulo `code.py.old1` possiede **10** funzioni ACTIVE, di cui **2** endpoint HTTP.  
Dipende da (chiamate uscenti cross-module): `code`.  
È usato da (chiamate entranti cross-module): `code`.

| Funzione | Firma | Route | Scopo |
|---|---|---|---|
| [`code.py.old1.animate_price_change`](#code.py.old1.animate_price_change) | `animate_price_change(old_price, new_price, color)` | `—` | Anima la transizione visiva tra due prezzi su un display MatrixPortal, mostrando un effetto di rullo per le cifre. |
| [`code.py.old1.connect_wifi`](#code.py.old1.connect_wifi) | `connect_wifi()` | `—` | Gestisce il tentativo di connessione WiFi con timeout, gestendo errori e restituendo esito. |
| [`code.py.old1.darker`](#code.py.old1.darker) | `darker(color, factor)` | `—` | Scurisce un colore moltiplicando le componenti R, G, B per un fattore (tipicamente <1) e ricomponendo l'intero packed RGB. |
| [`code.py.old1.format_high_low`](#code.py.old1.format_high_low) | `format_high_low(value)` | `—` | Converte un valore in intero e restituisce una stringa formattata con il simbolo $. |
| [`code.py.old1.format_price`](#code.py.old1.format_price) | `format_price(value)` | `—` | Converte un valore in intero e lo formatta con apostrofo come separatore delle migliaia e simbolo del dollaro finale. |
| [`code.py.old1.home`](#code.py.old1.home) | `home(request: Request)` | `GET /` | Restituisce la pagina home HTML che mostra lo stato attuale del display (acceso/spento) e offre i pulsanti per accenderlo/spegnelo. |
| [`code.py.old1.pad_left`](#code.py.old1.pad_left) | `pad_left(text, width)` | `—` | Aggiunge spazi a sinistra a text per raggiungere una lunghezza minima width, se necessario. |
| [`code.py.old1.reset_wifi`](#code.py.old1.reset_wifi) | `reset_wifi()` | `—` | Resetta la connessione WiFi spegnendo e riaccendendo la radio, poi richiama connect_wifi per la riconnessione. |
| [`code.py.old1.set_display_state`](#code.py.old1.set_display_state) | `set_display_state(state: bool)` | `—` | Attiva o disattiva la visualizzazione sul display: se False, cancella i testi; se True, ripristina i dati di prezzo e colori se presenti. |
| [`code.py.old1.toggle_display`](#code.py.old1.toggle_display) | `toggle_display(request: Request)` | `GET /toggle_display` | Gestisce il toggle del display via parametro query 'state' (on/off) e restituisce una pagina HTML di conferma con redirect automatico. |

---

<!-- fn:code.py.old1.animate_price_change -->
## `code.py.old1.animate_price_change` <a name="code.py.old1.animate_price_change"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `animate_price_change(old_price, new_price, color)`  
**Async**: no  
**Posizione**: `code.py.old1.py:162`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.pad_left`](#code.pad_left), [`code.py.old.pad_left`](#code.py.old.pad_left), [`code.py.old1.pad_left`](#code.py.old1.pad_left)  
**Chiamata da**: —  

**Scopo**: Anima la transizione visiva tra due prezzi su un display MatrixPortal, mostrando un effetto di rullo per le cifre.

**Input**: old_price: str | None (prezzo attuale, None diventa ""); new_price: str (nuovo prezzo); color: qualsiasi valore di colore accettato da matrixportal.

**Output**: Nessun valore di ritorno (None). Lancia eccezioni solo per errori interni (es. time.sleep o connessione display).

**Gotcha**: Se old_price è None, dopo pad_left si ottiene una stringa di spazi, causando un effetto di 'apparizione' dal nulla; solo i caratteri digit di new_price vengono animati, i non-numerici appaiono immediatamente.

<!-- fn:code.py.old1.connect_wifi -->
## `code.py.old1.connect_wifi` <a name="code.py.old1.connect_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `connect_wifi()`  
**Async**: no  
**Posizione**: `code.py.old1.py:40`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.py.old.reset_wifi`](#code.py.old.reset_wifi), [`code.py.old1.reset_wifi`](#code.py.old1.reset_wifi), [`code.reset_wifi`](#code.reset_wifi)  

**Scopo**: Gestisce il tentativo di connessione WiFi con timeout, gestendo errori e restituendo esito.

**Input**: nessun parametro

**Output**: True se connesso, False in caso di timeout o fallimenti; stampa messaggi di progresso/errore.

**Gotcha**: —

<!-- fn:code.py.old1.darker -->
## `code.py.old1.darker` <a name="code.py.old1.darker"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `darker(color, factor)`  
**Async**: no  
**Posizione**: `code.py.old1.py:67`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.py.old1.set_display_state`](#code.py.old1.set_display_state)  

**Scopo**: Scurisce un colore moltiplicando le componenti R, G, B per un fattore (tipicamente <1) e ricomponendo l'intero packed RGB.

**Input**: color: intero a 24 bit (RRGGBB); factor: float generalmente tra 0 e 1 (invariante implicito).

**Output**: Intero a 24 bit con il nuovo colore scurito; nessuna eccezione lanciata.

**Gotcha**: Se factor > 1, le componenti possono superare 255 e i bit in eccesso inquinano i campi adiacenti nel valore di ritorno; la funzione non esegue clamping.

<!-- fn:code.py.old1.format_high_low -->
## `code.py.old1.format_high_low` <a name="code.py.old1.format_high_low"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_high_low(value)`  
**Async**: no  
**Posizione**: `code.py.old1.py:153`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Converte un valore in intero e restituisce una stringa formattata con il simbolo $.

**Input**: value: qualsiasi tipo accettato da int() (es. str, float).

**Output**: Restituisce una stringa nel formato '<valore> $'. Può sollevare ValueError se il valore non è convertibile.

**Gotcha**: int() tronca i decimali, non arrotonda. Lo spazio prima del $ è incluso.

<!-- fn:code.py.old1.format_price -->
## `code.py.old1.format_price` <a name="code.py.old1.format_price"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `format_price(value)`  
**Async**: no  
**Posizione**: `code.py.old1.py:148`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Converte un valore in intero e lo formatta con apostrofo come separatore delle migliaia e simbolo del dollaro finale.

**Input**: value: qualsiasi tipo convertibile a int (str, float, int). ValueError se non convertibile.

**Output**: Stringa formattata (es. "1'234$"). Non solleva eccezioni dopo la conversione.

**Gotcha**: La conversione a int tronca la parte decimale, non arrotonda. L'apostrofo è usato come separatore delle migliaia.

<!-- fn:code.py.old1.home -->
## `code.py.old1.home` <a name="code.py.old1.home"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `home(request: Request)`  
**Async**: no  
**Posizione**: `code.py.old1.py:225`  
**Route**: `GET /` (auth: none)  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: —  

**Scopo**: Restituisce la pagina home HTML che mostra lo stato attuale del display (acceso/spento) e offre i pulsanti per accenderlo/spegnelo.

**Input**: request: oggetto Request di Flask (non utilizzato per estrarre dati, solo inoltrato al costruttore della Response).

**Output**: Response con content-type text/html e corpo contenente la pagina.

**Gotcha**: Richiede che la variabile globale `display_enabled` sia definita nel modulo; altrimenti solleva NameError.

<!-- fn:code.py.old1.pad_left -->
## `code.py.old1.pad_left` <a name="code.py.old1.pad_left"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `pad_left(text, width)`  
**Async**: no  
**Posizione**: `code.py.old1.py:157`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: —  
**Chiamata da**: [`code.animate_price_change`](#code.animate_price_change), [`code.py.old.animate_price_change`](#code.py.old.animate_price_change), [`code.py.old1.animate_price_change`](#code.py.old1.animate_price_change)  

**Scopo**: Aggiunge spazi a sinistra a text per raggiungere una lunghezza minima width, se necessario.

**Input**: text: stringa; width: intero >= 0

**Output**: Stringa con spazi preposti per raggiungere almeno width caratteri. Se text già soddisfa, invariato.

**Gotcha**: width negativo causa errore nella moltiplicazione di stringa; text deve essere stringa per concatenazione.

<!-- fn:code.py.old1.reset_wifi -->
## `code.py.old1.reset_wifi` <a name="code.py.old1.reset_wifi"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `reset_wifi()`  
**Async**: no  
**Posizione**: `code.py.old1.py:56`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.connect_wifi`](#code.connect_wifi), [`code.py.old.connect_wifi`](#code.py.old.connect_wifi), [`code.py.old1.connect_wifi`](#code.py.old1.connect_wifi)  
**Chiamata da**: —  

**Scopo**: Resetta la connessione WiFi spegnendo e riaccendendo la radio, poi richiama connect_wifi per la riconnessione.

**Input**: nessun parametro

**Output**: ritorna il valore booleano di connect_wifi(), oppure False se si verifica un'eccezione.

**Gotcha**: La radio viene spenta e riaccesa senza garanzia di successo; se connect_wifi fallisce dopo il reset, la connessione potrebbe rimanere assente.

<!-- fn:code.py.old1.set_display_state -->
## `code.py.old1.set_display_state` <a name="code.py.old1.set_display_state"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `set_display_state(state: bool)`  
**Async**: no  
**Posizione**: `code.py.old1.py:192`  
**Route**: —  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.darker`](#code.darker), [`code.py.old1.darker`](#code.py.old1.darker)  
**Chiamata da**: [`code.py.old1.toggle_display`](#code.py.old1.toggle_display)  

**Scopo**: Attiva o disattiva la visualizzazione sul display: se False, cancella i testi; se True, ripristina i dati di prezzo e colori se presenti.

**Input**: state: bool - stato desiderato del display

**Output**: None; modifica la variabile globale display_enabled.

**Gotcha**: Dipende da variabili globali preesistenti (display_enabled, last_price, last_high, last_low, price, previous_price_value, factor) e da matrixportal già inizializzato; non verifica la disponibilità di tali risorse.

<!-- fn:code.py.old1.toggle_display -->
## `code.py.old1.toggle_display` <a name="code.py.old1.toggle_display"></a>

**Stato**: `[ACTIVE]`  
**Firma**: `toggle_display(request: Request)`  
**Async**: no  
**Posizione**: `code.py.old1.py:243`  
**Route**: `GET /toggle_display` (auth: none)  
**Env**: —  
**Side-effects**: —  
**Chiama**: [`code.py.old1.set_display_state`](#code.py.old1.set_display_state)  
**Chiamata da**: —  

**Scopo**: Gestisce il toggle del display via parametro query 'state' (on/off) e restituisce una pagina HTML di conferma con redirect automatico.

**Input**: Richiede un oggetto Request con parametro query 'state' (valori attesi: 'on' o 'off').

**Output**: Restituisce sempre un oggetto Response con contenuto HTML (messaggio di conferma o errore). In caso di eccezione catturata, il body contiene il messaggio di errore.

**Gotcha**: La variabile globale display_enabled è dichiarata ma mai letta; lo stato effettivo è gestito esternamente da set_display_state().
