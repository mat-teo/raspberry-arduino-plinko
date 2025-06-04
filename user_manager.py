import json
import threading

FILE_UTENTI = "users.json"
file_lock = threading.Lock()  # lock globale per sincronizzare accesso al file

def carica_utenti():
    try:
        with open(FILE_UTENTI, "r") as f:
            data = json.load(f)
        return data.get("users", {})
    except FileNotFoundError:
        return {}

def salva_utenti(utenti):
    with file_lock:
        data = {"users": utenti, "esiti": carica_esiti()}
        with open(FILE_UTENTI, "w") as f:
            json.dump(data, f, indent=4)

def carica_esiti():
    with open(FILE_UTENTI, "r") as f:
        data = json.load(f)
    return data.get("esiti", [])

def salva_esiti(esiti):
    with file_lock:
        data = {"users": carica_utenti(), "esiti": esiti}
        with open(FILE_UTENTI, "w") as f:
            json.dump(data, f, indent=4)

def verifica_credenziali(username, password):
    utenti = carica_utenti()
    if username in utenti and utenti[username]["password"] == password:
        return True
    return False

def aggiungi_utente(username, password, name, surname):
    utenti = carica_utenti()
    if username in utenti:
        return False  # utente già esistente

    utenti[username] = {
        "password": password,
        "name": name,
        "surname": surname,
        "credit": "0",
        "event": ""
    }
    salva_utenti(utenti)
    return True

def get_credito(username):
    utenti = carica_utenti()
    return float(utenti.get(username, {}).get("credit", 0))

def aggiorna_credito(username, importo):
    utenti = carica_utenti()
    if username not in utenti:
        return False
    credito_attuale = float(utenti[username].get("credit", 0))
    credito_nuovo = credito_attuale + importo
    utenti[username]["credit"] = str(credito_nuovo)
    salva_utenti(utenti)
    return True

def aggiorna_evento(username, evento):
    utenti = carica_utenti()
    if username not in utenti:
        return False
    utenti[username]["event"] = evento
    salva_utenti(utenti)
    return True

def get_evento(username): 
    utenti = carica_utenti()
    return utenti.get(username, {}).get("event", "")

def push_esito(game):
    esiti = carica_esiti()
    esiti.append(game)
    salva_esiti(esiti)