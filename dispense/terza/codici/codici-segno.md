---
layout: page
title: "Codici: Numeri interi con segno"
permalink: /dispense/terza/codici/segno/
---

Con la codifica dei numeri naturali è impossibile codificare il simbolo `-`, dato che nel mondo dei computer esistono solamente i numeri binari. Per codificare i numeri relativi (sia positivi che negativi) le codifiche principali sono:

1. Modulo e segno
2. Complemento a 1
3. Complemento a 2

**Numeri positivi:** per tutte e tre le codifiche, una volta stabilito il numero di bit, si usa la stessa funzione dei numeri naturali. Il valore +56 codificato a 16 bit sarà `0000 0000 0011 1000` per tutte e tre.

---

## 1. Modulo e segno

Il **MSB** (bit più significativo) viene utilizzato per indicare il segno:

- MSB = 0 → segno + (numero positivo)
- MSB = 1 → segno - (numero negativo)

La funzione **MS(b)** inverte il MSB (la prima cifra da sinistra):

| Input               | MS(input)           |
|---------------------|---------------------|
| `0010`              | `1010`              |
| `1011000010`        | `0011000010`        |

**Regole:**

- Numeri positivi: si usa f^n(simb).
- Numeri negativi: si usa MS(f^n(simb)).

**Esempio:** codifica di -56 a 16 bit:

1. Si converte 56 in binario a 16 bit: `0000 0000 0011 1000`
2. Si applica MS: **1**`000 0000 0011 1000`

**Decodifica:**

1. Verificare il segno guardando il MSB.
2. Calcolare il modulo.

Esempi:

- `0000 0011 1110 1000` → MSB = 0 → positivo → +1000
- `1000 0011 1110 1000` → MSB = 1 → negativo → MS → `0111 1100 0001 0111` → -1000

**Limiti a 16 bit:**

| Proprietà                       | Valore  |
|---------------------------------|---------|
| Numero massimo                  | +32767 (2^15 - 1) |
| Numero minimo                   | -32767 (-(2^15 - 1)) |
| Doppia rappresentazione dello 0 | +0: `0000 0000 0000 0000`; -0: `1000 0000 0000 0000` |

---

## 2. Complemento a 1

Si codificano i numeri negativi **invertendo tutti i bit** del numero positivo (gli 0 diventano 1 e viceversa).

La funzione **CA1(b)** inverte tutti i bit:

| Input                         | CA1(input)                    |
|-------------------------------|-------------------------------|
| `0000 0000 0000 1010` (+10)   | `1111 1111 1111 0101` (-10)   |

**Esempio:** codifica di -56 a 16 bit:

1. Si converte 56: `0000 0000 0011 1000`
2. Si applica CA1: `1111 1111 1100 0111`

**Regole:**

- Numeri positivi: si usa f^n(simb).
- Numeri negativi: si usa CA1(f^n(simb)).

**Decodifica:**

1. Verificare il segno guardando il MSB.
2. Se negativo, applicare CA1 e convertire in decimale.

Esempi:

- `0000 0011 1110 1000` → positivo → +1000
- `1000 0011 1110 1000` → negativo → CA1 → `0111 1100 0001 0111` → -31767

**Perché solo ai numeri con MSB = 0?** Se applicassimo CA1 anche ai numeri con MSB = 1 otterremmo codici che rappresentano già numeri positivi. Esempio: 40000 → `1001 1100 0100 0000`, e CA1 darebbe `0110 0011 1011 1111` che rappresenta già 25535.

**Limiti a 16 bit:**

| Proprietà                       | Valore  |
|---------------------------------|---------|
| Numero massimo                  | +32767 (2^15 - 1) |
| Numero minimo                   | -32767 (-(2^15 - 1)) |
| Doppia rappresentazione dello 0 | +0: `0000 0000 0000 0000`; -0: `1111 1111 1111 1111` |

---

## 3. Complemento a 2

Si codificano i numeri negativi applicando il **Complemento a 1** e poi **sommando 1**.

La funzione **CA2(b) = CA1(b) + 1**

Esempio con +10 e -10 a 16 bit:

```
+10 → 0000 0000 0000 1010
-10 → CA1: 1111 1111 1111 0101
      + 1: 0000 0000 0000 0001
      ───────────────────────
      =    1111 1111 1111 0110
```

**Esempio:** codifica di -56 a 16 bit:

1. Si converte 56: `0000 0000 0011 1000`
2. Si applica CA1: `1111 1111 1100 0111`
3. Si somma 1: `1111 1111 1100 1000`

**Regole:**

- Numeri positivi: si usa f^n(simb).
- Numeri negativi: si usa CA2(f^n(simb)).

**Limiti a 16 bit:**

| Proprietà                       | Valore  |
|---------------------------------|---------|
| Numero massimo                  | +32767 (2^15 - 1) |
| Numero minimo                   | **-32768** (-(2^15)) |
| Doppia rappresentazione dello 0 | **No** |

**Perché non si ha una doppia rappresentazione dello zero?**

Applichiamo il procedimento a `1111 1111 1111 1111`:

1. Sommiamo 1 → `0000 0000 0000 0000`
2. CA1 → `1111 1111 1111 1111`

Risultato: `1111 1111 1111 1111` → -32768 (non è zero).

**Esempio completo:** codifica di -125 a 16 bit (complemento a 2):

```
125           → 0000 0000 0111 1101
CA1           → 1111 1111 1000 0010
CA1 + 1 = CA2 → 1111 1111 1000 0011
```

Cambio di rappresentazione del codice:

| Base    | +125 (`0000 0000 0111 1101`) | -125 (`1111 1111 1000 0011`) |
|---------|-------------------------------|-------------------------------|
| Base 16 | `007D`                        | `FF83`                        |
| Base 8  | `000175`                      | `177603`                      |

**Attenzione:** quando si cambia la rappresentazione del codice, non bisogna mai dimenticare lo scopo (rappresentare su 16 bit in complemento a 2). In base 8 si ottengono 18 bit (6 cifre ottali): bisogna scartare i 2 bit in più a sinistra.

---

## Confronto tra le tre codifiche (16 bit)

| Proprietà          | Modulo e segno | Complemento a 1 | Complemento a 2 |
|--------------------|----------------|------------------|------------------|
| Numero massimo     | +32767         | +32767           | +32767           |
| Numero minimo      | -32767         | -32767           | **-32768**       |
| Doppio zero        | Si             | Si               | **No**           |
| Funzione negativo  | MS(f^n(x))     | CA1(f^n(x))      | CA2(f^n(x))      |
