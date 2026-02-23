---
layout: page
title: "Codici: Definizione di codice"
permalink: /dispense/terza/codici/codice/
---

In informatica il codice viene utilizzato per legare due mondi: quello reale e quello del computer.

- **Codifica**: passaggio dal mondo reale a quello del computer.
- **Decodifica**: passaggio dal mondo del computer a quello reale.

> Un codice è un insieme di regole per convertire un'informazione in un altro oggetto o in un'altra azione, non necessariamente dello stesso tipo.

Esempi:

| Codice       | Tipo di informazione       | Si trasforma in    | Come?                                                     |
|--------------|----------------------------|--------------------|-----------------------------------------------------------|
| Semaforo     | Colore                     | Azione             | Rosso → _stop_; verde → _procedere_                      |
| Codice Morse | Sequenza di punti/linee    | Lettera/numero     | `...` → `S`; `---` → `O`; `...---...` → `SOS`           |

---

## Significante, valore e codice

Il numero 10 può assumere diverse **forme** (significanti):

| Rappresentazione  | Forma          |
|-------------------|----------------|
| Numeri arabi      | «10»           |
| Italiano          | «dieci»        |
| Inglese           | «ten»          |
| Numeri romani     | «X»            |
| Unario            | «IIIIIIIIII»   |
| Base 2            | «1010»         |
| Base 8            | «12»           |
| Base 16           | «A»            |

Nel mondo dei computer il numero diventa qualcosa di definito molto precisamente: si stabilisce **come** convertirlo in binario e in **quanti bit**.

Possibili codifiche del numero 10:

| Codifica              | Risultato                        |
|-----------------------|----------------------------------|
| 8 bit, MSB a sinistra | `0000 1010`                     |
| 16 bit, MSB a sinistra| `0000 0000 0000 1010`           |
| 8 bit, MSB a destra   | `0101 0000`                     |
| 16 bit, MSB a destra  | `0101 0000 0000 0000`           |

---

## Cambio di rappresentazione vs codifica

- **Cambio di rappresentazione**: convertire un numero in un'altra base senza ulteriore scopo.
- **Codifica**: convertire un'informazione in un'altra forma con uno **scopo** preciso.

Esempio: convertire 125 in base 2 dà `1111101`. Questa è una semplice conversione. Ma se lo scopo è _utilizzarlo con un computer a 16 bit_, il risultato diventa `0000 0000 0111 1101`. Avendo specificato lo scopo, abbiamo applicato una **codifica**.

Terminologia:

| Termine             | Significato                                                             |
|---------------------|-------------------------------------------------------------------------|
| **Valore**          | Il numero come quantità astratta, indipendente dalla rappresentazione   |
| **Rappresentazione**| Lo stesso valore scritto in modi diversi (base 2, 8, 10, 16)           |
| **Codice**          | Il valore rappresentato in una forma compatibile ad uno specifico scopo |

---

## Codice dei numeri naturali

I numeri naturali (N) sono i numeri interi positivi da 0 a infinito. La codifica converte il numero da base 10 a base 2 e aggiunge gli zeri necessari a raggiungere il numero di bit richiesti.

**Esempio:** il valore 56 in base 10:

| Base    | Rappresentazione |
|---------|------------------|
| Base 2  | `11 1000`        |
| Base 8  | `70`             |
| Base 16 | `38`             |

Codifica per un computer a 16 bit: `11 1000` → `0000 0000 0011 1000`

**Limiti:** con 16 bit il numero massimo codificabile è 2^16 - 1 = 65535.

### Rappresentazione in altre basi

Le basi 16 e 8 sono utili per **compattare** un numero binario in un formato più leggibile. In ogni caso, i computer usano sempre e solo i bit.

`0000 0000 0011 1000` rappresentato diversamente:

| Base    | Rappresentazione |
|---------|------------------|
| Base 16 | `0038`           |
| Base 8  | `00070`          |

**Attenzione** al procedimento inverso:

- `0038` (base 16) → in base 2 diventa esattamente `0000 0000 0011 1000` (il codice).
- `00070` (base 8) → in base 2 diventa `00 0000 0000 0011 1000`, con **2 zeri in più** che non esistono nel codice.

> Si deve sempre ricordare le regole della codifica applicata.

---

## Funzioni di codifica e decodifica

Abbiamo due mondi:

```
Mondo Reale (simboli)  ⟺  Mondo Computer (numeri binari)
```

- **c(simb) → b** : funzione di codifica, trasforma un simbolo in un numero binario.
- **d(b) → simb** : funzione di decodifica, trasforma un numero binario in un simbolo.

Definiamo **f^n(d)** la funzione che converte un numero decimale _d_ in un numero binario a _n_ bit:

| Funzione   | Risultato                  |
|------------|----------------------------|
| f(13)      | `1101`                     |
| f^5(13)    | `0 1101`                   |
| f^16(13)   | `0000 0000 0000 1101`      |

Se _n_ non è definito, si usa il minor numero possibile di bit.
