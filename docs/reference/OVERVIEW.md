# Function Reference — OVERVIEW (cosa fa il progetto, per aree)

> Data: `2026-07-21` · SHA: `b40b9be`  
> Generato da `funcref.overview` — sintesi grounded, ACTIVE-only. Le aree sono una sintesi tematica ancorata a moduli reali dell'inventario; i moduli citati esistono tutti (gate anti-allucinazione).

## Cosa fa

Sistema di visualizzazione prezzi su matrice LED via Flask: anima il passaggio tra vecchio e nuovo valore, formatta cifre con simbolo dollaro, gestisce la connettività WiFi del dispositivo e offre funzioni di manipolazione cromatica per il display.

## Aree / capability

### Animazione e formattazione prezzi

Mostra variazioni progressive del prezzo sul display a matrice, con formattazione in dollari (simbolo e separatore delle migliaia).

Moduli: [`code`](code.md)

### Connessione WiFi

Tenta la connessione alla rete WiFi con credenziali predefinite, restituendo l'esito entro un timeout di 20 secondi.

Moduli: [`code`](code.md)

### Manipolazione colori

Scurisce un colore RGB applicando un fattore di riduzione uniforme alle componenti.

Moduli: [`code`](code.md)

## Flussi chiave

_(nessun flusso seed definito)_
