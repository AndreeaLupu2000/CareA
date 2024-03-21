import threading
import subprocess
from gpiozero import Button
from time import sleep
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


# Initialize the button
pain_button = Button(27)
drink_button = Button(17)
chat_button = Button(2)
schedule_button = Button(3)
orientation_button = Button(4)

# Define a global process variable to manage the subprocess
pain_process = None
drink_process = None
chat_process = None
schedule_process = None
orientation_process = None



def start_drink():
    global drink_process
    while True:
        drink_button.wait_for_press()
        print("Start the drink.py...")
        drink_process = subprocess.Popen(["python", "drink.py"])
        sleep(2)

        drink_button.wait_for_press()
        drink_process.terminate()
        drink_process = None
        sleep(2)



def start_schedule():
    global schedule_process
    while True:
        schedule_button.wait_for_press()
        print("Start the schedule.py...")
        schedule_process = subprocess.Popen(["python", "schedule.py"])
        sleep(2)

        schedule_button.wait_for_press()
        schedule_process.terminate()
        schedule_process = None
        sleep(2)



def start_orientation():
    global orientation_process
    while True:
        orientation_button.wait_for_press()
        print("Start the orientation.py...")
        orientation_process = subprocess.Popen(["python", "orientation.py"])
        sleep(2)

        orientation_button.wait_for_press()
        orientation_process.terminate()
        orientation_process = None
        sleep(2)


def start_chat():
    global chat_process
    while True:
        chat_button.wait_for_press()
        print("Start the chat.py...")
        chat_process = subprocess.Popen(["python", "chat.py"])
        sleep(2)

        chat_button.wait_for_press()
        chat_process.terminate()
        chat_process = None
        sleep(2)


def start_pain():
    global pain_process
    while True:
        pain_button.wait_for_press()
        print("Start the pain.py...")
        pain_process = subprocess.Popen(["python", "pain.py"])
        sleep(2)

        pain_button.wait_for_press()
        pain_process.terminate()
        pain_process = None
        sleep(2)

def run_function():
    while True:
        try:
            if pain_button.is_pressed:
                start_pain()
            elif drink_button.is_pressed:
                start_drink()
            elif chat_button.is_pressed:
                start_chat()
            elif schedule_button.is_pressed:
                start_schedule()
            elif orientation_button.is_pressed:
                start_orientation()
        except KeyboardInterrupt:
            break


def run_patient_screen():
    subprocess.run(["python3", "patient_screen.py"])


app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)


@app.route('/')
def index():
    return render_template('ns-interface.html')



def run_nurse_station():
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


# Thread for running the patient_screen.py script
t_patient_screen = threading.Thread(target=run_patient_screen)
t_nurse_station = threading.Thread(target=run_nurse_station)
t_chat = threading.Thread(target=start_chat)
t_pain = threading.Thread(target=start_pain)
t_drink = threading.Thread(target=start_drink)
t_schedule = threading.Thread(target=start_schedule)
t_orientation = threading.Thread(target=start_orientation)

socketio.run(app, host='10.183.71.160', port=5000, debug=False, allow_unsafe_werkzeug=True)

# Start the patient_screen.py script thread
t_patient_screen.start()
t_nurse_station.start()
t_chat.start()
t_pain.start()
t_drink.start()
t_schedule.start()
t_orientation.start()