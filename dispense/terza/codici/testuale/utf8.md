---
layout: page
title: Codifica UTF-8
permalink: /dispense/terza/utf8/
---

La codifica UTF-8 (Unicode Transformation Format) funziona sempre con una tabella codepoint-simbolo, ma la tabella è lunga **1.112.064** righe. Con soli 7 bit non è possibile rappresentare tutti i caratteri.

La codifica UTF-8 è a **lunghezza variabile**: la parola di codice può essere lunga 1, 2, 3 o 4 byte.

---

## 1. Compatibilità con ASCII

I codepoint di valore ≤ 127 della tabella UTF-8 sono gli stessi della tabella ASCII, preceduti da un bit `0`:

| Carattere | ASCII      | UTF-8           |
|-----------|------------|-----------------|
| `C`       | `100 0011` | **0**`100 0011` |

> I caratteri ASCII vengono rappresentati in UTF-8 con **un solo byte** perché sono i più **frequenti**: è intelligente associare ai caratteri più frequenti una parola di codice di lunghezza minore.

---

## 2. Codepoint > 127

I codepoint maggiori di 127 **non** vengono codificati direttamente in binario:

- ❌ `È` → 200 → `1100 1000` → `0000 0000 1100 1000`

Questo perché quando si decodifica, bisogna poter capire **senza ambiguità** dove ogni parola inizia e finisce. La codifica reale è:

- ✅ `È` → 200 → `1100 0011 1000 1000`

Spiegazione dei bit:

```
1100 0011 1000 1000
###^ ^^^^ ##^^ ^^^^
```

- `#` = bit di controllo: `110` indica l'inizio del primo byte, `10` indica un byte di continuazione.
- `^` = bit che rappresentano il valore del codepoint (200).

> Con 2 byte si perdono 5 bit per i bit di controllo, quindi si possono rappresentare solo 2^11 codepoint invece di 2^16.

---

## 3. Tabella riassuntiva UTF-8

| Prefisso | Byte | Formato                                     | Codepoint          |
|----------|------|---------------------------------------------|--------------------|
| `0`      | 1    | `0XXX XXXX`                                 | 0 - 127 (ASCII)    |
| `110`    | 2    | `110X XXXX  10XX XXXX`                      | 128 - 2.047        |
| `1110`   | 3    | `1110 XXXX  10XX XXXX  10XX XXXX`           | 2.048 - 65.535     |
| `1111 0` | 4    | `1111 0XXX  10XX XXXX  10XX XXXX  10XX XXXX`| 65.536 - 1.112.064 |

> **Importante**: in una codifica si deve tenere conto anche della fase di decodifica, ovvero permettere al decodificatore di comprendere facilmente l'inizio e la fine di ogni parola di codice, soprattutto quando la lunghezza è variabile.

---

## 4. Frequenza e lunghezza della parola di codice

Il principio alla base di UTF-8 è: **caratteri più frequenti = parole di codice più corte**.

| Byte | Caratteri inclusi                        | Frequenza d'uso | Esempio          |
|------|------------------------------------------|-----------------|------------------|
| 1    | Lettere latine, cifre, punteggiatura     | Altissima        | `a`, `0`, `.`    |
| 2    | Lettere accentate, greco, cirillico, ecc.| Alta             | `è`, `ñ`, `ü`   |
| 3    | CJK (cinese, giapponese, coreano), ecc.  | Media            | `漢`, `あ`, `한` |
| 4    | Emoji, simboli rari, scritture storiche  | Bassa            | `😀`, `𐍈`       |

Questo approccio minimizza la dimensione media dei file: un testo in italiano, composto prevalentemente da caratteri ASCII e poche lettere accentate, occuperà circa 1 byte per carattere.
