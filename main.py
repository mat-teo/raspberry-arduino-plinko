import threading
from app import flask_thread
from bluetooth_handler import bluetooth_thread

if __name__ == '__main__':
    thread_bt = threading.Thread(target=bluetooth_thread, daemon=True)
    thread_flask = threading.Thread(target=flask_thread, daemon=True)

    thread_bt.start()
    thread_flask.start()

    thread_bt.join()
    thread_flask.join()