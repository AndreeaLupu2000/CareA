from flask import Flask, render_template
from flask_socketio import SocketIO
from gpiozero import Button
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def on_button_press():
    socketio.emit('button_press', {}, namespace='/')


def listen_for_button():
    button = Button(27)
    while True:
        button.wait_for_press()
        on_button_press()

if __name__ == '__main__':
    Thread(target=listen_for_button).start()
    socketio.run(app, host='192.168.0.120', port=5000, debug=True)
