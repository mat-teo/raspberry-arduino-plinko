# Progetto Scolastico: **[PLINKO!]**

## Sommario
- [Obiettivi del Progetto](#obiettivi-del-progetto)
- [Descrizione del Progetto](#descrizione-del-progetto)
- [Ruoli e Responsabilità](#ruoli-e-responsabilità)
- [Timeline del Progetto](#timeline-del-progetto)
- [Risorse](#risorse)
- [Rischi e Mitigazioni](#rischi-e-mitigazioni)
- [Risultati Attesi](#risultati-attesi)
- [Conclusioni](#conclusioni)

---

## Obiettivi del Progetto
- **Obiettivo Principale**: Ricreare il famoso gioco PLINKO, giocabile in una struttura fisica di legno, controllabile tramite interfaccia Flask in esecuzione su un raspberry per scommettere sui risultati, e con l'ausilio di una scheda ESP
- **Obiettivi Specifici**:
  1. Ricreare la struttura
  2. Permettere di utilizzare l'ESP per giocare le partite e leggere i risultati
  3. Realizzare l'interfaccia tramite flask per permettere all'utente la gestione delle partite e delle scommesse


## Descrizione del Progetto
Il progetto consiste nella realizzazione di un sistema di gioco interattivo che simula fisicamente il gioco Plinko.
La pallina reale scende lungo una struttura in legno, e l’intero processo è controllato da un Raspberry Pi, che comunica via Bluetooth con una scheda ESP.
Il Raspberry gestisce i crediti, avvia le partite e raccoglie i risultati, il tutto tramite un’interfaccia web sviluppata in Flask.
Ogni utente può accedere all’interfaccia per avviare una partita e scommettere sui risultati, in un contesto sicuro e controllato.
Il progetto unisce hardware e software in una soluzione integrata, educativa e coinvolgente.

## Ruoli e Responsabilità
| Nome                  | Ruolo                     | Responsabilità                           |
|-----------------------|---------------------------|--------------------------------------------|
| Artifoni Matteo   | Gestione login, connessione bluetooth lato raspberry e threading      | Garantire il funzionamento di registrazione e login, una concorrenza dei thread sincronizzata e una connessione bluetooth stabile         |
| Shkina Fabian   | Realizzazione della struttura e implementazione dei sensori      | Realizzare struttura in legno che emuli il gioco PLINKO!, implementare la corretta lettura dei risultati tramite i 7 sensori a infrarossi        |
| Paletta Andrea   | Lettura del risultato dal raspberry, modifiche credito utente e comunicazione esiti      | Assicurare l'avvenuta lettura dell'esito della partita, modificare il credituo dell'utente di conseguenza e comunicarlo all'utente         |
| Inzoli Leonardo   | Interfaccie web tramite flask, gestione delle route e gestione connessione bluetooth lato ESP      | Realizzare un'interfaccia semplice e intuitiva web per l'esperienza utente, gestire le route di flask e il loro utilizzo e garantire connettività stabile dal lato ESP         |

## Timeline del Progetto
| Fase                  | Data di Inizio  | Data di Fine  | Stato        |
|-----------------------|----------------|---------------|--------------|
| Analisi    | 28/03/2025         | 28/03/2025        | Completata |
| Sviluppo    | 04/04/2025         | 23/05/2025        | Completata |
| Test e bug fix        | 23/05/2025         | 30/05/2025        | Completata |
| Consegna e documentazion    | 30/05/2025         | 04/06/2025        | Completata |

## Risorse
- **Strumenti e Software**:
    Linguaggio: Python (per il backend e Flask)
    Librerie: Flask, threading, pybluez (per comunicazione Bluetooth)
    Software: VS code, browser web
    Tecnologie: SSH, per comunicazione wireless con il raspberry
    Framework: Flask per l’interfaccia utente

- **Componenti Hardware**:
    Scheda ESP
    Raspberry pi
    Struttura PLINKO in legno
    Servomotori e sensori

#### materiali

| Materiale                  | Costo  |
|-----------------------|----------------|
| ESP    | 150€        |
| Raspberry    | 800€         |
| Sensori infrarossi        | 70€         |
| Servomotore        | 20€         |
| Legno        | 20€         |


Totale : 1060€

#### Calcolo costo personale
4 studenti * 10€/h (indicativi) * 12 h = 480€

Costo totale progetto: 1540€

## Rischi e Mitigazioni

| Rischio               | Probabilità | Impatto  | Mitigazione                              |
|-----------------------|--------------|----------|------------------------------------------|
| Comunicazione Bluetooth instabile           | Media | Alta | Testare più moduli Bluetooth, usare timeout e retry            |
| Errore nel riconoscimento del risultato fisico           | Alta | Alta | Corretta implementazione dei sensori o validazione doppia del risultato            |

## Risultati Attesi
Sistema funzionante di Plinko fisico con interfaccia web

Gestione utenti e crediti integrata

Partite avviabili da più utenti in maniera sicura e tracciata

Sistema affidabile, con aggiornamenti in tempo reale dell’interfaccia

Esperienza utente semplice, accessibile e stabile

## Conclusioni
Il progetto PLINKO! integra in modo efficace hardware e software per creare un’esperienza di gioco interattiva, didattica e tecnologicamente avanzata.
È un esempio concreto di come concetti di programmazione, gestione hardware e interfacce utente possano essere applicati in un contesto reale.
