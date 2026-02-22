---
layout: page
title: Codepoint e tabella di conversione
permalink: /dispense/terza/codepoint/
---

Ogni carattere, a seconda della codifica, viene rappresentato da un numero corrispondente alla sua posizione nella tabella di conversione. Tale numero è detto **codepoint**.

> _A code point, codepoint or code position is a particular position in a table, where the position has been assigned a meaning._
> — [Wikipedia](https://en.wikipedia.org/wiki/Code_point)

Ad esempio, la codifica ASCII utilizza una tabella di 128 righe, dove ad ogni riga è associato un simbolo:

| Riga | Simbolo |
|------|---------|
| 0    | `NULL`  |
| 48   | `0`     |
| 65   | `A`     |
| 97   | `a`     |

- Dalla riga _0_ alla riga _31_ (inclusa): caratteri **non stampabili**, ovvero caratteri non visibili ma utili per definire inizio e fine di un testo o di una linea.
- Dalla riga _32_ alla riga _127_ (inclusa): caratteri **stampabili**.

Esempio di un estratto della tabella:

| Decimale | Esadecimale | Simbolo | Descrizione   |
|----------|-------------|---------|---------------|
| 114      | 72          | r       | Lowercase r   |
| 115      | 73          | s       | Lowercase s   |
| 116      | 74          | t       | Lowercase t   |
| 117      | 75          | u       | Lowercase u   |
| 118      | 76          | v       | Lowercase v   |
| 119      | 77          | w       | Lowercase w   |
| 120      | 78          | x       | Lowercase x   |
| 121      | 79          | y       | Lowercase y   |
| 122      | 7A          | z       | Lowercase z   |
| 123      | 7B          | {       | Opening brace |
| 124      | 7C          | \|      | Vertical bar  |
| 125      | 7D          | }       | Closing brace |
| 126      | 7E          | ~       | Tilde         |
| 127      | 7F          | DEL     | Delete        |
