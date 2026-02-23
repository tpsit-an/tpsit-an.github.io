---
layout: page
title: HTTP
permalink: /dispense/quinta/http/http/
---

# HTTP

**Autore:** Lorenzo Principi

**Argomenti necessari:**
- Thread.
- Socket.

---

## 1. Lo stack TCP/IP con HTTPS

È utile avere un'idea generale di ciò che avviene durante una comunicazione in rete. In questo capitolo approfondiremo il protocollo `HTTP` del livello *applicazione*. Appartenendo al livello più alto dello stack a quattro livelli, <u>per ogni</u> <u>comunicazione</u> operano *"al di sotto"* del livello *applicazione* altri tre livelli. Questo significa che in una comunicazione concreta ciascun livello utilizza un protocollo specifico utilizzando meccanismi di identificazione propri. Questo si traduce nella pratica in un pacchetto di byte composto nel seguente modo:

```
   PHYSICAL layer          NETWORK layer             TRANSPORT layer
   (Ethernet)              (IP)                      (TCP)
  ├──────────────────────┼────────────────────────┼──────────────────────┤
   EC 02 73 D0 CF 00      45 00 00 28 8A F2 40      B1 E4 01 BB 47 7D
   10 E1 8E 46 2B 4E      00 40 06 10 2D 0A C8      41 97 20 91 E6 79
   08 00                   A0 F9 B9 0F 3A E0         50 10 02 21 9F CB
                                                     00 00
```

Dove nel caso del protocollo `HTTP` i protocolli usati sono i seguenti, con relativi *target* e relativa *codifica*:

```
 livello         │ protocollo          │ codifica target / target
─────────────────┼─────────────────────┼─────────────────────────────
 APPLICATION     │ HTTP                │ URL / risorsa
─────────────────┼─────────────────────┼─────────────────────────────
 TRANSPORT       │ TCP                 │ (IP, PORTA) / endpoint
─────────────────┼─────────────────────┼─────────────────────────────
 NETWORK         │ IP                  │ IP address / host
                 │ (Internet Protocol) │
─────────────────┼─────────────────────┼─────────────────────────────
 PHYSICAL        │ Ethernet, Wifi      │ MAC address / nodo di rete¹
```

¹ Come una Network Interface Card (NIC), ovvero la scheda di rete.

Come si può notare dallo stack, il target del protocollo indica il tipo di obbiettivo che ogni protocollo ha in una comunicazione. Nel protocollo `TCP` l'obbiettivo è un altro *endpoint*, nel protocollo `IP` un altro *host*, nel protocollo `HTTP` invece l'obbiettivo è una *risorsa*.

Guardando il pacchetto `HTTP` possiamo notare come non siano presenti dei byte dedicati al livello applicazione. Questo accade in quanto il livello *applicazione* è un livello *astratto*, ovvero i dati che invia sono inclusi nel livello trasporto.


### Cos'è una risorsa

Come abbiamo già detto, la *risorsa* è l'obbiettivo del protocollo `HTTP`. Ma cos'è una risorsa? Nello standard `RFC3986`[^1] è definita come segue:

> [...] il termine "risorsa" è utilizzato in senso generale per indicare qualsiasi elemento identificabile tramite un URI. Esempi familiari includono un documento elettronico, un'immagine, una fonte di informazioni con uno scopo coerente (ad esempio, "le previsioni del tempo di oggi per Los Angeles"), un servizio (ad esempio, un gateway da HTTP a SMS) e una raccolta di altre risorse. Una risorsa non è necessariamente accessibile tramite Internet; ad esempio, anche gli esseri umani, le società e i libri rilegati in una biblioteca possono essere risorse. [...]

Come si può notare da tale definizione, le risorse non sono accessibili esclusivamente tramite Internet.

[^1]: https://datatracker.ietf.org/doc/html/rfc3986


### Codifica delle risorsa: URI

Le risorse vengono codificate con lo standard Uniform Resource Identifier (`URI`). Tale codifica identifica una risorsa come una stringa, ovvero una sequenza di caratteri codificati in `US-ASCII`. Nello standard `RFC3986` la `URI` viene definita come:

> A Uniform Resource Identifier (URI) is a compact sequence of characters that identifies an abstract or physical resource.

Nel caso del protocollo `HTTP` viene usato un sottoinsieme delle `URI`, gli Uniform Resource Locator (`URL`).


### Uniform Resource Locator (URL)

Il termine *locator* nell'acronimo `URL` sta ad indicare che nella stringa viene anche definita la modalità con cui si dovrà accedere alla risorsa, e tale modalità è il protocollo. Lo standard `URI` non è stato creato appositamente per il protocollo `HTTP`, infatti le `URL` possono essere usate anche con altri protocolli (`ftp://` o `ssh://`).


### URL nel protocollo HTTP

Le `URL` utilizzate nel protocollo `HTTP` (e `HTTPS`) specificano un modo di accedere alla risorsa che coinvolge due operatori:
- L'operatore *client* che <u>chiede</u> la risorsa.
- L'operatore *server* che <u>fornisce</u> la risorsa.

Ecco un esempio di `URL` completa con protocollo `HTTP`:

```
 http://         www.iisve.it        /tool/cerca        ?tipo=cerca&cerca_sito=esami        #risultati
 ──┬────         ─────┬─────        ─────┬─────        ────────────┬───────────────        ─────┬────
   │                  │                  │                         │                            │
   ▼                  ▼                  ▼                         ▼                            ▼
url::protocol    url::authority     url::path               url::query                  url::fragment
```

- `url::protocol`: protocollo della comunicazione a livello applicazione.
- `url::authority`: l'autorità che possiede la risorsa.
- `url::query`: lista di attributi `chiave:valore` separati da `&`.
- `url::fragment`: riferimento ad una sezione della pagina `HTML`.

**Campo `url::query`.** Il campo `url::query` è suddiviso in parametri aventi la seguente forma:

> `chiave:valore`

Possono esservi più parametri, in tal caso questi sono suddivisi dal carattere `&`. La sintassi è quindi la seguente:

```
?‹nome_p1›=‹valore_p1›[&‹nome_p2›=‹valore_p2›...]
```

dove le parentesi quadre indicano che possono esserci uno o più parametri.

**Attenzione:** `url::query` non è obbligatorio.


### Campi obbligatori della URL

Gli unici campi dell'`URL` che non sono opzionali sono `url::protocol` e `url::authority`.


### Nota su authority

`url::authority` non è da confondere con il dominio, anche se spesso nei browser vediamo solamente quest'ultimo. In modo esteso essa è definita nel seguente modo:

> `user:password@host:porta`

Nel protocollo `HTTP`, `user` e `password` sono <u>vietati</u>, perciò potrà essere solamente: `host:porta`.

Per quanto riguarda `porta`, anche questo è spesso omesso in quanto impostato automaticamente ad `80` per l'`HTTP` e `443` per l'`HTTPS`.

**Attenzione:** Un server può comunque accettare comunicazioni `HTTP` o `HTTPS` su porte differenti da 80 e 443 rispettivamente. In tali casi `porta` dovrà essere specificato, come ad esempio durante la fase di development di siti web si utilizzano server locali in ascolto sulla porta 3000 (`https://localhost:3000`).

---

## 2. Protocollo HTTP(s)

Il protocollo HyperText Transfer Protocol (`HTTP`)[^2] è un protocollo applicazione utilizzato da due operatori per eseguire operazioni su una risorsa definita dalla `URL`:
- Due operatori, il *client* ed il *server*.
- Una risorsa, definita dalla `URL`.
- Un metodo, ovvero la tipologia di operazione da fare sulla risorsa.

[^2]: In questa dispensa non abbiamo bisogno di distinguere tra `HTTP` e `HTTPS`, per cui useremo solamente il termine `HTTP`, valido per entrambi i protocolli.

Tali operatori comunicano a livello di trasporto con un socket `TCP`.

### Panoramica di una comunicazione HTTP

Il protocollo `HTTP` è un ciclo che parte dal *client*, il quale ha necessità di effettuare un'operazione su una risorsa posseduta da un altro operatore raggiungibile tramite rete internet, detto *server*. Tale operazione può essere sia di modifica o di sola acquisizione.

1. Il *client* genera un documento testuale chiamato *request* (`REQ`): qui dentro mette tutte le informazioni necessarie per descrivere l'operazione che vuole effettuare sulla risorsa:
   - `req::url::path`: specifica il *nome* della risorsa posseduta dal *server*;
   - `req::method`: la tipologia di operazione;
   - `req::url::query` e `req::body`: i dati[^3] che servono per effettuare tale operazione;
   - `req::header`: altre informazioni di configurazione come, ad esempio, la codifica utilizzata per i dati nel `req::body` o lo stato di autenticazione.
2. La `REQ` viene inviata dal *client* al *server*.
3. Il *server* riceve la `REQ`.
4. Il *server* legge `req::url::path` per trovare la risorsa cui si riferisce il *client*:
   - Se `req::url::path` identifica una risorsa che <u>non</u> esiste, allora genera una *response* (`RES`) con errore `[404, NOT FOUND]`, e la invia al *client*.
   - Se `req::url::path` identifica una risorsa che esiste, prosegue allo step 5.
5. Il *server* legge `req::method` e **verifica** che la funzione che gestisce tale `req::method` su tale risorsa sia <u>implementata</u>:
   - Se non è implementata il *server* genera una `RES` con `res::code` uguale a `[405, METHOD NOT ALLOWED]` e la invia al *client*.
   - Se invece è implementata prosegue allo step 6.
6. Il *server* ora **verifica** che il *client* abbia i sufficienti permessi per effettuare l'operazione di tipo `req::method` su tale risorsa.
   - Se il *client* non è autorizzato, il *server* genera una `RES` con errore `[401, UNAUTHORIZED]` e la invia al *client*.
   - Se il *client* è autorizzato prosegue allo step 7.
7. Il *server* legge i dati contenuti in `req::query` e/o `req::body`:
   - Se i dati non sono come se li aspetta (*validi*), il *server* genera una `RES` con `res::code` uguale a `[400, BAD REQUEST]` e la invia al *client*.
   - Se i dati sono come se li aspetta prosegue allo step 8.
8. Il *server* effettua infine l'operazione sulla risorsa:
   - In questa fase se si generano degli errori non è più a causa della `REQ` ma dei possibili bug presenti nell'implementazione della funzione che gestisce la `REQ` <u>nel</u> *server*. In caso di errori, il *server* genera una `RES` con `res::code` uguale a `[500, SERVER ERROR]` e la invia al *client*.
   - Se tutto va liscio il *server* genera una `RES` con `res::code` uguale a `[200, OK]` e la invia al *client*.

[^3]: Esempio: nel `req::body` vanno username e password in un form di login; in `req::url::query` va il testo da ricercare quando si effettua una ricerca.

Quando il *client* riceve la `RES`:
- Verifica l'esito attraverso `res::code`.
- Se aveva richiesto di ricevere dei dati dal *server* legge `res::body`[^4] decodificandolo secondo quanto indicato negli `res::header`.

[^4]: Non esiste `query` nella response.

Infine il *client* utilizza i dati ricevuti secondo i propri scopi. Esempi semplici: se era un'operazione di *acquisizione* dati può mostrare i dati ricevuti (come una pagina `HTML`), se era un'operazione di modifica della risorsa può avvertire che l'operazione nel *server* è andata a buon fine, o in caso contrario comunicare l'eventuale errore.


### 2.1 Protocollo HTTP nei vari livelli dello stack

**Livello di trasporto: socket TCP.** Il protocollo `HTTP` agisce a livello di trasporto adottando un socket `TCP` il quale funge da ponte comunicativo tra il *client* ed il *server*. Il *client* si connette, il *server* è in ascolto per eventuali connessioni in ingresso:

```
         client                                   server (8.7.6.5)
──────────────────────────────────       ──────────────────────────────────
 s = socket(AF_INET, SOCK_STREAM)        sp = socket(AF_INET, SOCK_STREAM)
 s.connect(("8.7.6.5", 443))  ───────>  sp.bind(("8.7.6.5", 443))
 s.send(request)               ──────>  sp.listen()
 response = s.recv(BS)                   sa = sp.accept()
 s.close()                    <──────    request = sa.recv(BS)
                                         response = elabora(request)
 # utilizza response                     sa.send(response)
 # secondo i suoi scopi                  sa.close()
```

Dove `BS` è una variabile intera a cui diamo un valore generale in quanto non è centrale durante questa spiegazione.

**La risorsa è sempre posseduta dal server.** Questo è molto importante. Si immagini il *server* composto almeno da due elementi principali:
- Un programma che esegue l'endpoint `HTTP`, ovvero un socket `TCP` in ascolto di uno o più *client*.
- Un sistema di archiviazione (persistenza):
  - Un programma che esegue il Database.
  - Un programma che esegue il File storage.

Al contempo *client* è un programma che esegue un socket `TCP`.

**Livello applicazione: ciclo *request* e *response*.** Dato che è il *server* a fornire la risorsa al *client* che la richiede, il protocollo `HTTP` a livello applicazione funzionerà come segue:

1. Il client genera la *request* (`REQ`): un documento testuale codificato in `US-ASCII`.
2. Attraverso il socket `TCP` invia `REQ` al *server*.
3. Il *server* riceve `REQ` e la elabora generando una *response* (`RES`), sempre codificata in `US-ASCII`.
4. Il *client* riceve `RES` e la utilizza per i propri scopi.

Questo è sintetizzato nella seguente immagine:

```
 ┌──────────────┐                              ┌──────────────────────────────────────┐
 │    client     │          TCP                 │               server                  │
 │              ├═══════════════════════════════┤                                      │
 │              │       ■                    ■  │                                      │
 │  ┌────────┐  │                               │  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │
 │  │        │  │                               │  │  REQ                         │   │
 │  │  REQ   │  │    REQ                        │  │   │                          │   │
 │  │        │  │  ──────────────────────────>  │  │   ▼                          │   │
 │  │  RES   │  │                               │  │  ┌───────────────────────┐   │   │
 │  │        │  │                               │  │  │ RES = elabora(REQ)    │───┼─┐ │
 │  └────────┘  │    RES                        │  │  └───────────────────────┘   │ │ │
 │   PROGRAMMA  │  <──────────────────────────  │  │   │                          │ │ │
 │              │                               │  │   ▼                          │ │ │
 │              │                               │  │  RES              PROGRAMMA  │ │ │
 │              │                               │  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘ │ │
 │              │                               │       ┌───────────────────┐       │ │
 │              │                               │       │   File storage    │<──────┘ │
 │              │                               │       └───────────────────┘       │ │
 │              │                               │       ┌───────────────────┐       │ │
 │              │                               │       │     Database      │<──────┘ │
 │              │                               │       └───────────────────┘         │
 └──────────────┘                              └──────────────────────────────────────┘
```

Si può notare come sia centrale la funzione `elabora(REQ)` la quale restituisce la `RES` a seconda della `REQ` <u>creata dal client</u>. In questa funzione, è possibile ma non obbligatorio che il *server* interagisca con il database ed il file storage.


### 2.2 Scambio di dati tra client e server

Il *client* ha due possibilità per inviare dati dinamici al server:
- Il campo `req::url::query`: parametri codificati nell'`URL`. In `req::url::query` vengono mandati dati quando questi sono pochi e hanno lunghezza (in byte) piccola.
- Il campo `req::body`: qui va qualsiasi dato, da una pagina `html` codificata in `UTF-8` ai byte di un'immagine `jpg`.

Il *server* invece invia i dati solamente attraverso il `req::body`.

**La request.** La request (`REQ`) è un file testuale codificato in `US-ASCII` strutturato nel seguente modo:
- La prima riga contiene i seguenti campi separati da un carattere spazio:
  - `req::method`: la tipologia di operazione sulla risorsa[^5].
  - `req::url`: la `URL`. I campi della `URL` nella `REQ` sono identificati così: ad esempio `url::query` diventa `req::url::query`.
  - `req::version`: la versione del protocollo `HTTP` (es: «`http/2.0`»).
- `req::header`: dalla seconda riga fino al carattere `[CRLF]`[^6]: ciascuna riga rappresenta un *header*, campi di configurazione in forma: «`nome header:valore header`».
- `req::body`: campo che può essere opzionale (non esiste se `req::method` è `GET`). Contiene dati inviati dal *client* al *server* codificati (il tipo di codifica è descritto nell'header `content-type`, si veda la tabella content-type).

[^5]: Possibili valori sono: `GET/POST/DELETE/OPTIONS/PUT/PATCH`.
[^6]: Indica una riga composta solamente dai caratteri Carriage Return (CR) e Line Feed (LF), in pratica è una riga vuota.

La seguente immagine mostra un esempio con body codificato in `JSON`:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  req::method     req::url                                   req::version  │
│  ┌──────┐        ┌──────────────────────────────────────┐   ┌────────┐   │
│  │ POST │        │ https://iisve.it/cerca?testo=5BI#..  │   │http/2.0│   │
│  └──────┘        └──────────────────────────────────────┘   └────────┘   │
│                                                                           │
│  ┐  header 1   accept-encoding: gzip,deflate,br,zstd                     │
│  │  header 2   accept-language: en-US,en;q=0.9              req::header   │
│  │  header 3   content-type: application/json                             │
│  │  header 4   content-length: 33                                         │
│  ┘  header 5   user-agent: Mozilla/5.0 (X11; ...                         │
│     [CRLF]                                                                │
│                                                                           │
│  req::body     { "messaggio": "Hello World!" }                            │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

**La response.** La response (`RES`) è un file testuale codificato in `US-ASCII` strutturato nel seguente modo:
- La prima riga contiene i seguenti campi separati da un carattere spazio:
  - `res::version`: la versione del protocollo `HTTP` («`http/2.0`»).
  - `res::code`, un codice numerico che identifica l'esito della `REQ`.
  - `res::reason`, ovvero la spiegazione testuale dell'esito.
- `res::header`: come nella `REQ`, dalla seconda riga fino al carattere `[CRLF]`.
- `res::body`: campo può essere opzionale, contiene i dati inviati dal *server* al *client*.

```
┌───────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  res::version    res::code    res::reason                                 │
│  ┌────────┐      ┌─────┐     ┌───────────┐                              │
│  │http/2.0│      │ 404 │     │ Not found │                              │
│  └────────┘      └─────┘     └───────────┘                              │
│                                                                           │
│  ┐  header 1   accept-encoding: gzip,deflate,br,zstd                     │
│  │  header 2   accept-language: en-US,en;q=0.9              res::header   │
│  │  header 3   content-type: application/json                             │
│  │  header 4   content-length: 33                                         │
│  ┘  header 5   user-agent: Mozilla/5.0 (X11; ...                         │
│     [CRLF]                                                                │
│                                                                           │
│  res::body     { "messaggio": "Page not found in my data!" }              │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```


**Request e response: body.** `body` è il *corpo* della `REQ` o `RES`. Esso trasporta i dati che il *client* vuole trasmettere al *server* e viceversa. La codifica del `body` è definita negli `header`:
- `content-length`: numero di byte del body (sia nella `REQ` che nella `RES`).
- `content-type`: codifica del body, si veda la tabella seguente.

**Attenzione:** Il body non è presente nelle `REQ` quando `req::method` è `GET`.

| Contenuto body  | `content-type`             |
|-----------------|----------------------------|
| Immagini jpg    | `image/jpg`                |
| Immagini png    | `image/png`                |
| Pagina `HTML`   | `text/html`                |
| File `CSS`      | `text/css`                 |
| File Javascript | `text/javascript`          |
| File binari     | `application/octet-stream` |

**Response: status code.** Il campo `res::code`, detto *status code* è un codice numerico di tre cifre, presente nella prima riga della `RES`. Esso indica l'<u>esito</u> della richiesta e separato da uno spazio c'è `res::reason`, ovvero la descrizione testuale dello *status code*.

Di seguito vengono elencati i vari range di *status code*:
- Esito *successful*, range `200-299`: indica che la richiesta è stata elaborata con successo dal *server*.
- Esito *client error*, range `400-499`: indica che la richiesta del *client* non può essere soddisfatta perché non valida. Un esempio comune è quando il *client* chiede una pagina web che non esiste: `404 - Not Found Error`.
- Esito *server error*, range `500-599`: indica che la richiesta del *client* non può essere soddisfatta a causa di errori verificatisi nel *server*.

---

## 3. Metodi

La definizione di metodo, contenuto nel campo `req::method`, è la seguente:

> Un metodo definisce il tipo di operazione che il *client* richiede al *server* di effettuare sulla risorsa definita dall'`URL`.

**Metodo GET.** Il metodo `GET` definisce una richiesta per <u>ottenere</u> una risorsa definita dall'`URL`. Peculiarità di una request `GET`:
- `req::body` è vuoto.
- L'unico modo per il *client* di inviare dati è il campo `req::url::query`.
- Il *server* invia i dati in `res::body`. La codifica del body è definita in un header di `res::header` dal nome `content-type`.

Esempi di utilizzo:
- Navigazione web: ogni pagina viene ottenuta tramite request `GET`.
- Immagini: ogni immagine visualizzata in una pagina viene ottenuta dopo richiesta `GET`.
- Ricerche: il testo da ricercare viene passato dal *client* attraverso i parametri di `req::url::query`.

**Metodo POST.** Il metodo `POST` definisce una richiesta per <u>modificare</u>, <u>creare</u>, <u>eliminare</u> la risorsa definita in `req::url`.
- `req::body` non è vuoto e viene usato per inviare i dati. Può contenere dati strutturati (`XML`, `JSON`), immagini, testo, eccetera.
- `req::query` solitamente è inutilizzato.

Esempi di utilizzo:
- Autenticazione: quando un utente si autentica per effettuare il *login* in un sito la richiesta è `POST`.
- Modifica stato dello studente: quando si modifica se uno studente è presente, presente fuori aula, ecc...
- Quando si carica un'immagine di profilo.
- Quando si effettua il logout.
- Quando si crea un contenuto su un social network o sito in generale.
