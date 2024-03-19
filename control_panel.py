from gpiozero import Button
import subprocess
from time import sleep

button = Button(2)

process = None


def start_process():
    global process
    print("Start the nurse_station.py...")
    process = subprocess.Popen(["python", "nurse_station.py"])


def stop_process():
    global process
    print("Stop the nurse_station.py...")
    if process is not None:
        process.terminate()
        process = None


button.wait_for_press()
start_process()

sleep(2)

button.wait_for_press()
stop_process()
