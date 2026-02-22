---
layout: page
title: Codifica delle immagini
permalink: /dispense/terza/immagini/
---

Le immagini digitali sono sequenze di bit che rappresentano i colori dei singoli pixel. Esistono diverse codifiche, tra cui bitmap (non compressa) e JPEG (compressa).

**Indice:**

1. [Codifica bitmap](#1-codifica-bitmap)
2. [Codifica JPEG](#2-codifica-jpeg)

---

## 1. Codifica bitmap

Nella codifica bitmap ogni pixel viene memorizzato singolarmente:

```
uint8 immagine[R][C];      // bianco e nero (1 byte per pixel)
uint8 immagine[R][C][3];   // colori RGB (3 byte per pixel)
```

Ogni pixel a colori è composto da 3 canali: **R** (rosso), **G** (verde), **B** (blu), ciascuno rappresentato da un valore intero da 0 a 255 (8 bit).

---

## 2. Codifica JPEG

Un'immagine bitmap da 10 megapixel occupa circa:

> 10 MP × 3 byte per pixel = 30 MB

Questa dimensione è spesso troppo grande per l'archiviazione e la trasmissione. Per questo è necessaria una codifica compressa come **JPEG**, che riduce significativamente la dimensione del file sacrificando parte della qualità visiva (compressione con perdita).
