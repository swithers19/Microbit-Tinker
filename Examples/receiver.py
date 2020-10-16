#RECEIVER CODE
from microbit import *
import music
import radio

radio.on()

while True:
    incoming = radio.receive()
    if incoming == "up":
        music.play(music.FUNK)
        sleep
    elif incoming == "shake":
        music.play(music.WAWAWAWAA)