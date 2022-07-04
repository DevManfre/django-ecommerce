# django-ecommerce
Lingua: :it:
## Obiettivo
Creazione un portale di e-commerce per la vendita di attrezzi e prodotti da palestra online (stile Decathlon ma specifico per la palestra).
L'e-commerce deve supportare i seguenti punti:
1. presenza di utenti anonimi che possono navigare per il sito e visualizzare i prodotti con il relativo presso e votazioni degli altri utenti;
2. presenza di una registrazione come fornitore o come acquirente;
3. ogni utente registrato da acquirente può visualizzare recensioni di altri utenti, confrontare prodotti simili, votare e lasciare recensioni per il prodotto e votare il fornitore;
4. ogni utente registrato come fornitore deve poter vedere informazioni (analytics) sugli acquisti di tutti i prodotti che ha messo in vendita;
5. presenza di un meccanismo di ricerca che permetta di selezionare i prodotti in base a diverse caratteristiche (prezzo, categoria, offerte…);
6. presenza di un sistema di recommendation basato su prezzi, caratteristiche simili, suggerimenti…

I punti facoltativi sono:
1. presenza del meccanismo di “carrello”, gli utenti registrati come acquirenti possono aggiungere prodotti al carrello, confermare acquisto di tutto il carrello o di una parte di esso. Il checkout prevede pagamento tramite bonifico. Il venditore riceve una notifica rispetto al nuovo acquisto e può confermare pagamento e spedizione effettuata. L’acquirente riceve una notifica di spedizione effettuata e può confermare la ricezione del prodotto.
2. presenza di una cronologia di ordini (in stile amazon) che permetta all’acquirente di visualizzare tutti i prodotti da lui precedentemente comprati.
3. funzionalità di forum al sito: possibilità per gli utenti di porre domande ai fornitori o domande alle quali possono rispondere altri clienti. Inserire la ricezione di notifiche quando si riceve una risposta. Aggiungere la possibilità di seguire un thread nel forum e ricevere notifiche quando ci sono nuovi post ai thread seguiti e mail di riassunto con periodicità impostabile.

## Avvio
- Avviare pipenv con il comando 'pipenv shell'
- Installare tutte le librerie necessarie con 'pipenv install'
- Avviare il server con il comando 'python manage.py runserver'
- In caso dia errore con il database, bisogna:
    - Commentare le chiamate di creazione ed eliminazione del DB;
    - Eseguire una migrazione con 'python manage.py migrate'
    - Decommentare le chiamate commentate precedentemente

