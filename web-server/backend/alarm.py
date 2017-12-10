
import device

def setAlarm(hours, minutes):
    print("set alarm for: "+hours+":"+minutes)
    triggerAlarm();
    
def triggerAlarm():
    print("Alarm triggered")
    device.playSound("Short-ring.mp3")

