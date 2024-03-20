import threading
import subprocess
from gpiozero import Button
from time import sleep

# Initialize the button
button = Button(27)

# Define a global process variable to manage the subprocess
process = None


def start_process():
    global process
    print("Start the sts.py...")
    process = subprocess.Popen(["python", "sts.py"])


def stop_process():
    global process
    print("Stop the sts.py...")
    if process is not None:
        process.terminate()
        process = None


def run_patient_screen():
    # This function will run the patient_screen.py continuously.
    subprocess.run(["python3", "patient_screen.py"])


def manage_sts_script():
    global process

    button.wait_for_press()
    start_process()
    sleep(1)  # Debounce delay

    button.wait_for_press()
    stop_process()


# Thread for running the patient_screen.py script
t1 = threading.Thread(target=run_patient_screen)

# Thread for managing the sts.py script
t2 = threading.Thread(target=manage_sts_script)

# Start the patient_screen.py script thread
t1.start()

# Start the sts.py management thread
t2.start()

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
