from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from time import sleep
from gpiozero import Button
from threading import Thread

button_chat = Button(2)
button_pain = Button(4)
button_drink = Button(3)
button_schedule = Button(17)
button_orientation = Button(19)

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('ns-interface.html')


def listen_for_button():
    global button_chat
    global button_pain
    global button_drink
    global button_schedule
    global button_orientation


    while True:
        try:
            if button_chat.is_pressed:
                print("Chat button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'chat', namespace='/')
            elif button_pain.is_pressed:
                print("Pain button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'pain', namespace='/')
            elif button_drink.is_pressed:
                print("Drink button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'drink', namespace='/')
            elif button_schedule.is_pressed:
                print("Schedule button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'schedule', namespace='/')
            elif button_orientation.is_pressed:
                print("Orientation button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'orientation', namespace='/')
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    Thread(target=listen_for_button).start()
    socketio.run(app, host='127.0.0.1', port=5000, debug=False, allow_unsafe_werkzeug=True)