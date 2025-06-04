from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import shared_data
from bluetooth_handler import connettiti, check_bluetooth, start_new_game
import user_manager
from time import sleep
import threading
from game_manager import start_game

app = Flask(__name__)
app.secret_key = "supersegreta"
app.permanent_session_lifetime = 60 * 60 * 24 * 7  # 7 giorni

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember") == "on"

        if user_manager.verifica_credenziali(username, password):
            session.permanent = remember
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", errore="Credenziali errate")

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username").strip()
        password = request.form.get("password")
        name = request.form.get("name").strip()
        surname = request.form.get("surname").strip()

        if not username or not password or not name or not surname:
            return render_template("register.html", errore="Tutti i campi sono obbligatori")

        if not user_manager.aggiungi_utente(username, password, name, surname):
            return render_template("register.html", errore="Username già esistente")

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']
    credito_utente = user_manager.get_credito(username)

    status = connettiti()
    return render_template('index.html', connesso=status, credito=credito_utente, username=username,last3 = user_manager.carica_esiti()[-3:])

@app.route('/checkBluetooth')
def check_bluetooth_route():
    return check_bluetooth()

@app.route('/getStatus')
def get_status():
    check_bluetooth()
    return shared_data.status

@app.route('/get_credito')
def get_credito():
    if "username" not in session:
        return jsonify({"success": False, "message": "Non loggato"}), 401
    
    username = session["username"]
    credito = user_manager.get_credito(username)
    return jsonify({"success": True, "credito": credito})

@app.route('/aggiorna_credito', methods=['POST'])
def aggiorna_credito_route():
    if "username" not in session:
        return jsonify({"success": False, "message": "Non loggato"}), 401

    data = request.json
    ricarica = data.get("ricarica")
    if ricarica is None:
        return jsonify({"success": False, "message": "Importo ricarica mancante"}), 400

    try:
        ricarica = float(ricarica)
    except:
        return jsonify({"success": False, "message": "Importo ricarica non valido"}), 400

    username = session["username"]

    success = user_manager.aggiorna_credito(username, ricarica)
    if not success:
        return jsonify({"success": False, "message": "Utente non trovato"}), 400

    nuovo_credito = user_manager.get_credito(username)
    return jsonify({"success": True, "nuovo_credito": nuovo_credito})

@app.route('/newgame',methods=['POST'])
def new_game():
    if "username" not in session:
        return jsonify({"success": False, "message": "Non loggato"}), 401

    data = request.json
    bet = data.get("bet")
    if bet is None:
        return jsonify({"success": False, "message": "Importo scommessa mancante"}), 400
    
    bet = float(bet)
    start_new_game()
    sleep(0.2)
    thread_game = threading.Thread(target=start_game,args=(session["username"],bet) ,daemon=True)
    thread_game.start()
    print("new game started!")
    return "ok"

@app.route('/checkEvento')
def check_evento():
    if "username" not in session:
        return jsonify({"success": False, "message": "Non loggato"}), 401

    username = session["username"]
    esito = user_manager.get_evento(username)
    if esito == "":
        return jsonify({"success": True, "esito": None})

    user_manager.aggiorna_evento(username, "")
    return jsonify({"success": True, "esito": esito})


def flask_thread():
    print("[Flask] Thread avviato")
    app.run(host='0.0.0.0', port=5000, debug=False)