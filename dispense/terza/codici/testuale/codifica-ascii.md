---
layout: page
title: Codifica ASCII
permalink: /dispense/terza/codifica-ascii/
---

La codifica ASCII è semplicemente la codifica del codepoint (numero di riga) del carattere in 7 bit. Il numero di riga è senza segno.

| Proprietà                  | Valore                               |
|----------------------------|--------------------------------------|
| Alfabeto sorgente          | Caratteri stampabili e non stampabili |
| Alfabeto codice            | {0, 1}                               |
| Lunghezza parola di codice | **Fissa**, 7 bit                     |
| Righe nella tabella        | 128 codepoint                        |

---

## 1. Codifica di un carattere

1. Dato un simbolo, si cerca il codepoint corrispondente nella tabella.
2. Si converte il codepoint (numero decimale tra 0 e 127) in una parola di codice di 7 bit.

**Esempi:**

| Simbolo    | Codepoint | Parola di codice |
|------------|-----------|------------------|
| `NULL`     | 0         | `000 0000`       |
| `0`        | 48        | `011 0000`       |
| _new-line_ | 13        | `000 1101`       |

---

## 2. Decodifica di un carattere

1. Data una parola di codice a 7 bit, la si converte in numero decimale (codepoint).
2. Si cerca nella tabella il simbolo corrispondente a quel codepoint.

---

## 3. Esempio: codifica di una stringa

Una stringa è una sequenza di caratteri. Codifichiamo in ASCII la stringa:

```
ciao
Ciro da...
```

| Binario   | Carattere     |
|-----------|---------------|
| `1000011` | `C`           |
| `1101001` | `i`           |
| `1100001` | `a`           |
| `1101111` | `o`           |
| `0001010` | `\n` (a capo) |
| `1000011` | `C`           |
| `1101001` | `i`           |
| `1110010` | `r`           |
| `1101111` | `o`           |
| `0100000` | ` ` (spazio)  |
| `1100100` | `d`           |
| `1100001` | `a`           |
| `0100000` | ` ` (spazio)  |
| `0101110` | `.`           |
| `0101110` | `.`           |
| `0101110` | `.`           |

In binario la stringa diventa una sequenza continua di bit:

```
1000011 1101001 1100001 1101111 0001010 1000011 1101001 ...
C       i       a       o       \n      C       i
```
