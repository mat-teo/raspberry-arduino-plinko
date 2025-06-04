import bluetooth
import threading
import shared_data
from time import sleep

sock = None
data = None

def bluetooth_thread():
    global sock, data
    print("[Bluetooth] Thread avviato")
    while True:
        # crea e assegna 'sock'
        print("[Bluetooth] Tentativo di connessione...")
        connettiti()
        while True:
            try:
                if sock is not None and is_socket_open():
                    msg = sock.recv(1024)
                    if not msg:
                        print("[Bluetooth] Connessione chiusa.")
                        shared_data.status = "NON CONNESSO"
                        break
                    else:
                        shared_data.status = "CONNESSO"
                    msg = msg.decode(errors="ignore")
                    if msg == "2":
                        shared_data.esito = "L"
                        shared_data.isInGame = False
                    elif msg == "3":
                        shared_data.esito = "S"
                        shared_data.isInGame = False
                    elif msg == "4":
                        shared_data.esito = "H"
                        shared_data.isInGame = False
                    elif msg == "5":
                        shared_data.esito = "W"
                        shared_data.isInGame = False
                    elif msg == "6":
                        shared_data.esito = "H"
                        shared_data.isInGame = False
                    elif msg == "7":
                        shared_data.esito = "S"
                        shared_data.isInGame = False
                    elif msg == "8":
                        shared_data.esito = "L"
                        shared_data.isInGame = False
                    shared_data.status = "CONNESSO"
                    data = msg
                    print("[Bluetooth] Ricevuto:", msg)
                else:
                    print("[Bluetooth] Socket non valido.")
                    shared_data.status = "NON CONNESSO"
                    break

            except bluetooth.btcommon.BluetoothError as e:
                print("[Bluetooth] Errore di connessione:", e)
                shared_data.status = "NON CONNESSO"
                if sock:
                    try: sock.close()
                    except: pass
                    sock = None
                break

        print("[Bluetooth] Riprovo tra 2 secondi...")
        sleep(2)
    print("[Bluetooth] Thread terminato")


def connettiti():
    global sock
    #addr = "14:33:5C:52:D3:82"
    addr = "70:B8:F6:98:1F:02"

    try:
        if sock:
            try: sock.close()
            except: pass
            sock = None

        service_matches = bluetooth.find_service(address=addr)
        if len(service_matches) == 0:
            print("[Bluetooth] Nessun servizio trovato")
            return False

        match = service_matches[0]
        port = match["port"]
        host = match["host"]

        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))

        print("[Bluetooth] Connesso al dispositivo")
        shared_data.status = "CONNESSO"
        sock.send("9".encode())
        return True
    except Exception as e:
        print("[Bluetooth] Errore durante la connessione:", e)
        if sock:
            try: sock.close()
            except: pass
            sock = None
        return False


def is_socket_open():
    global sock
    try:
        sock.send(b'')
        return True
    except:
        return False


def start_new_game():
    global sock
    sock.send('1'.encode())
    shared_data.isInGame = True
    shared_data.esito = ""


def check_bluetooth():
    global sock
    if sock is None:
        shared_data.status = "NON CONNESSO"
        return "NON CONNESSO"
    try:
        sock.send("l".encode())
        print("[Bluetooth] Connessione attiva")
    except bluetooth.btcommon.BluetoothError as e:
        print("[Bluetooth] Connessione persa:", e)
        shared_data.status = "NON CONNESSO"
        try:
            sock.close()
        except:
            pass
        sock = None
        return "NON CONNESSO"
    
    shared_data.status = "CONNESSO"
    return "CONNESSO"
