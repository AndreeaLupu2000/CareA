import RPi.GPIO as GPIO
import subprocess

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 18
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
process = None


def button_pressed_callback(channel):
    global process
    if process is None:
        # Start the script
        process = subprocess.Popen(["/home/andreea/Documents/Master/WS23-24/TMS/CareA/sts.py"])
    else:
        # Stop the script
        process.terminate()  # or process.kill() if terminate doesn't work
        process = None


GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed_callback, bouncetime=200)

try:
    input("Press enter to quit\n\n")
finally:
    GPIO.cleanup()
