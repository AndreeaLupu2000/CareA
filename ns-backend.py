from flask import Flask, render_template
from flask_socketio import SocketIO
from time import sleep
from gpiozero import Button
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('ns-interface.html')


def on_button_press():
    sleep(5)
    socketio.emit('press', namespace='/')


def listen_for_button():
    button = Button(27)
    while True:
        button.wait_for_press()
        on_button_press()


if __name__ == '__main__':
    Thread(target=listen_for_button).start()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
