---
layout: page
title: Codifiche testuali
permalink: /dispense/terza/ascii/
---

Le codifiche testuali si effettuano codificando ogni singolo simbolo di un testo, detto _carattere_. Il testo verrà infine codificato come una sequenza di caratteri.

Vedremo due codifiche:

| Codifica | Lunghezza parola di codice |
|----------|---------------------------|
| ASCII    | fissa, 7 bit              |
| UTF-8    | variabile (1-4 byte)      |

**Concetti chiave:**

| Concetto              | Definizione                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Carattere             | Singolo simbolo di un testo (lettera, cifra, segno di punteggiatura, ecc.) |
| Codepoint             | Numero di riga associato a un carattere nella tabella di conversione        |
| Parola di codice      | Sequenza di bit che rappresenta un codepoint                                |
| Lunghezza fissa       | Ogni parola di codice ha la stessa lunghezza (es. ASCII, 7 bit)            |
| Lunghezza variabile   | Le parole di codice hanno lunghezze diverse (es. UTF-8, 1-4 byte)          |
| Bit di controllo      | Bit usati per indicare l'inizio e la continuazione di una parola (UTF-8)   |
| Frequenza e lunghezza | Caratteri più frequenti hanno parole di codice più corte (principio UTF-8) |

---

## Argomenti

1. [Codepoint e tabella di conversione](/dispense/terza/codepoint/)
2. [Codifica ASCII](/dispense/terza/codifica-ascii/)
3. [Codifica UTF-8](/dispense/terza/utf8/)
