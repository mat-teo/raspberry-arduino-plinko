import shared_data
import user_manager
from time import sleep

def start_game(username, bet):
        while shared_data.isInGame == True:
                sleep(1)
                print("partita in corso!")
        print("partita finita!")
        if shared_data.esito == "W": #2x (vinci il doppio di quello che hai scommesso)
                print(comunicazioneEsito(username, shared_data.esito, bet))
                esito = {"esito": shared_data.esito, "player":username,"bet": str(bet*2), "show": comunicazioneEsito(username, shared_data.esito, bet)}
        if shared_data.esito == "L": #0x (hai perso tutto)
                esito = {"esito": shared_data.esito, "player":username,"bet": str(bet), "show": comunicazioneEsito(username, shared_data.esito, bet)}
        if shared_data.esito == "H": #1.5x (vinci quello che hai scommesso più metà)
                user_manager.aggiorna_credito(username, bet + bet/2) 
                esito = {"esito": shared_data.esito, "player":username,"bet": str(bet*3/2), "show": comunicazioneEsito(username, shared_data.esito, bet)}
        if shared_data.esito == "S": #0.5x (vinci metà di quello che hai scommeso)
                user_manager.aggiorna_credito(username, bet + bet/2) 
                esito = {"esito": shared_data.esito, "player":username,"bet": str(bet/2), "show": comunicazioneEsito(username, shared_data.esito, bet)}
    
        print(comunicazioneEsito(username, shared_data.esito, bet))        
        sleep(1)

        user_manager.aggiorna_evento(username, shared_data.esito + " " + str(bet))

        sleep(1)

        user_manager.push_esito(esito)

def comunicazioneEsito(username,esito,bet):
    if esito == "W": #2x (vinci il doppio di quello che hai scommesso)
            return (username + " ha vinto " + str(bet*2) + " euro")
    if esito == "L": #0x (hai perso tutto)
            return (username + " ha perso " + str(bet) + " euro")
    if esito == "H": #1.5x (vinci quello che hai scommesso più metà)
            return (username + " ha vinto " + str(bet * 3 / 2) + " euro")
    if esito == "S": #1.5x (vinci quello che hai scommesso più metà)
            return (username + " ha vinto " + str(bet / 2) + " euro") 
                

    