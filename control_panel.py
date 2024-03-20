import threading
import subprocess
from gpiozero import Button
from time import sleep

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


def start_pain():
    global pain_process
    print("Start the pain.py...")
    pain_process = subprocess.Popen(["python", "pain.py"])
    sleep(2)

    pain_button.wait_for_press()
    pain_process.terminate()


def start_drink():
    global drink_process
    print("Start the drink.py...")
    drink_process = subprocess.Popen(["python", "drink.py"])
    sleep(2)

    drink_button.wait_for_press()
    drink_process.terminate()


def start_chat():
    global chat_process
    print("Start the chat.py...")
    chat_process = subprocess.Popen(["python", "chat.py"])
    sleep(2)

    chat_button.wait_for_press()
    chat_process.terminate()


def start_schedule():
    global schedule_process
    print("Start the schedule.py...")
    schedule_process = subprocess.Popen(["python", "schedule.py"])
    sleep(2)

    schedule_button.wait_for_press()
    schedule_process.terminate()


def start_orientation():
    global orientation_process
    print("Start the orientation.py...")
    orientation_process = subprocess.Popen(["python", "orientation.py"])
    sleep(2)

    orientation_button.wait_for_press()
    orientation_process.terminate()


def run_patient_screen():
    subprocess.run(["python3", "patient_screen.py"])


def run_nurse_station():
    subprocess.run(["python3", "ns-backend.py"])


def manage_sts_script():
    while True:
        if pain_button.is_active:
            start_pain()
        elif drink_button.is_active:
            start_drink()
        elif chat_button.is_active:
            start_chat()
        elif schedule_button.is_active:
            start_schedule()
        elif orientation_button.is_active:
            start_orientation()


# Thread for running the patient_screen.py script
t1 = threading.Thread(target=run_patient_screen)
t2 = threading.Thread(target=run_nurse_station)
t3 = threading.Thread(target=manage_sts_script)

# Start the patient_screen.py script thread
t1.start()
t2.start()
t3.start()

# These joins aren't strictly necessary unless you have a reason to wait for the threads to finish
# which generally isn't the case for daemon-like threads that are meant to run until the main program exits.
# t1.join()
# t2.join()


"""
from gpiozero import Button
from time import sleep
import subprocess

process_sts = None
process_patient_screen = None

def simple_test():
    button = Button(27)

    button.wait_for_press()
    process_sts = subprocess.Popen(["python", "sts.py"])
    sleep(1)

    button.wait_for_press()
    process_sts .terminate()

process_patient_screen = subprocess.Popen(["python", "patient_screen.py"])

simple_test()
"""
