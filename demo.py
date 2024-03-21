from chat_patient import shared_display
import pygame
import time

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


display = shared_display
time.sleep(5)
display.update_text(f"I heard: Where is the hospital cafeteria?")
time.sleep(2)
display.update_text(f"Response: Exit the room to the right,\n go to the elevator and take it to the ground floor. "
                    f"The cafeteria will be right in front of you.\n")
play_mp3('C:\\Users\\40732\\Desktop\\Education\\Master\\WS 23-24\\Think Make Start\\CareA\\demo.mp3')

time.sleep(1000)
