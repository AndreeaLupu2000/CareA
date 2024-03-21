import threading
import subprocess
from gpiozero import Button
from time import sleep


chat_button = Button(2)
chat_process = None


def run_patient_screen():
    subprocess.run(["python3", "patient_screen.py"])


def run_demo_audio():
    global chat_process
    chat_button.wait_for_press()
    print("Start the demo.py...")
    chat_process = subprocess.Popen(["python", "demo_audio.py"])
    sleep(2)

    chat_button.wait_for_press()
    print("Stop the demo.py...")
    chat_process.kill()
    chat_process = None
    sleep(2)

t_patient_screen = threading.Thread(target=run_patient_screen)
t_function = threading.Thread(target=run_demo_audio)

t_patient_screen.start()
t_function.start()

