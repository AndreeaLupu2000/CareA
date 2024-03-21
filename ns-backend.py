from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from time import sleep
from gpiozero import Button
from threading import Thread

chat_button = Button(2)
pain_button = Button(4)
drink_button = Button(3)
schedule_button = Button(17)
orientation_button = Button(19)

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('ns-interface.html')


def listen_for_button():
    global chat_button
    global pain_button
    global drink_button
    global schedule_button
    global orientation_button

    while True:
        try:
            if chat_button.is_pressed:
                print("Chat button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'chat', namespace='/')
            elif pain_button.is_pressed:
                print("Pain button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'pain', namespace='/')
            elif drink_button.is_pressed:
                print("Drink button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'drink', namespace='/')
            elif schedule_button.is_pressed:
                print("Schedule button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'schedule', namespace='/')
            elif orientation_button.is_pressed:
                print("Orientation button pressed")
                sleep(3)  # Simulate delay
                socketio.emit('pressed', 'orientation', namespace='/')
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    Thread(target=listen_for_button).start()
    socketio.run(app, host='10.183.71.160', port=5000, debug=False, allow_unsafe_werkzeug=True)