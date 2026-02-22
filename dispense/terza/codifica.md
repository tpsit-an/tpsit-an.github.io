---
layout: page
title: Codifica
permalink: /dispense/terza/codifica/
---

La codifica è il processo di rappresentazione di informazioni (testi, numeri, immagini) in una sequenza di bit.

> **I file sono sempre una sequenza lineare di bit.**

---

## Argomenti

- [Codifiche testuali](/dispense/terza/ascii/) — ASCII e UTF-8
- [Codifica delle immagini](/dispense/terza/immagini/) — Bitmap e JPEG

---

## Codifica testuale vs codifica numerica

Il numero 2.018.209.281.029 (13 cifre) richiede:

| Codifica               | Calcolo           | Bit necessari |
|------------------------|-------------------|---------------|
| Testuale (ASCII)       | 13 cifre × 7 bit | 91 bit        |
| Numerica (senza segno) | log2 del valore   | ~41 bit       |

La scelta della codifica dipende dal tipo di dato e dall'uso che se ne deve fare.
