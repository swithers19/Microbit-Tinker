#SENDER CODE
from microbit import *
import radio

radio.on()

while True:
    gesture = accelerometer.current_gesture()
    radio.send(gesture)
    
    if gesture == "face up":
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
