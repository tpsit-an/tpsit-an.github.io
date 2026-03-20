# Esempio: due client, un server

La situazione è la seguente: ci sono due client, _client-1_ e _client-2_, che vogliono effettuare una richiesta al server _server-1_.

## Connessione (accept/connect)

- [ ] Leggere il codice del server e del client
- [ ] Capire il ruolo di `accept` e `connect`
- [ ] Capire cosa significa "bloccante"

Il server _server-1_ è in ascolto:

``` python
# server
sp = socket(AF_INET, SOCK_STREAM)
sp.bind((IP_SERVER, 443))
sp.listen()
sa = sp.accept() # bloccante: attende una connessione in ingresso
```

Il client _client-1_ esegue la funzione `connect`:

``` python
# client-1
sock_client.connect((IP_SERVER, 443)) # bloccante: attende che il server accetti
```

La funzione `accept` si sblocca e ritorna un socket attivo `sa` connesso a _client-1_:

=== "Server"

    ``` python
    # server
    sa = sp.accept() # ✓ si sblocca
    ```

=== "Client"

    ``` python
    # client-1
    sock_client.connect((IP_SERVER, 443)) # ✓ si sblocca
    ```

!!! success "Connessione stabilita"
    Ora il socket `sa` nel server può scambiare pacchetti TCP con il socket `sock_client` nel client.

## Scambio dati (send/recv)

- [ ] Leggere il codice di `send` e `recv`
- [ ] Capire il meccanismo di sblocco tramite ACK
- [ ] Leggere il diagramma di sequenza

Successivamente, entrambi si ri-bloccano:

=== "Client"

    ``` python
    # client-1
    sock_client.connect((IP_SERVER, 443))
    sock_client.send(request) # bloccante: attende l'ACK dal server
    ```

=== "Server"

    ``` python
    # server
    sa = sp.accept()
    request = sa.recv(BS) # bloccante: attende i dati dal client
    ```

Quando il server riceve i dati inviati dalla `send`, la `recv` si sblocca. Lo sblocco del client avviene quando riceve l'`ACK`[^1] dal server.

[^1]: L'**ACK** (acknowledgment) è un pacchetto TCP inviato automaticamente dal kernel per confermare la ricezione dei dati.

``` mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    Note over C: send(request)
    C->>S: DATA
    Note over S: recv() si sblocca
    Note over S: invio ACK
    S->>C: ACK
    Note over C: send() si sblocca
```

<figcaption>Le frecce rappresentano il tempo di trasmissione dei pacchetti sulla rete.</figcaption>

## Elaborazione della richiesta

- [ ] Capire cosa fa il server dopo aver ricevuto la richiesta
- [ ] Capire cosa fa il client mentre aspetta

Ora il server effettua le operazioni sulla richiesta, mentre _client-1_ non fa nulla — aspetta la risposta.

*[TCP]: Transmission Control Protocol
*[HTTP]: HyperText Transfer Protocol
*[ACK]: Acknowledgment
*[URL]: Uniform Resource Locator
*[CPU]: Central Processing Unit
