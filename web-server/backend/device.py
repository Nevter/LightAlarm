"""
device.py file
Controlls the LEDs and plays sounds
"""

#from backend import ledcontroller
#from backend import soundcontroller
import ledcontroller
import soundcontroller

def setLED(colour, brightness):
    ledcontroller.setLEDs(colour, brightness)

def playSound(sound):
    soundcontroller.play(sound)
