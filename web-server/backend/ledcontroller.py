"""
ledcontroller.py
Controls the LEDs
"""

import RPi.GPIO as GPIO

redPin   = 11
greenPin = 13
bluePin  = 15

def setLEDs(colour, brightness):
	if brightness == '1': #turn on
		if colour == "red":
			print ("turning on red LED")
			turnOn(redPin)
		elif colour == "blue":
			print ("turning on blue LED")
			turnOn(bluePin)
		elif colour == "green":
			print ("turning on green LED")
			turnOn(greenPin)
	elif brightness == '0': #turn off
		if colour == "red":
			print ("turning off red LED")
			turnOff(redPin)
		elif colour == "blue":
			print ("turning off blue LED")
			turnOff(bluePin)
		elif colour == "green":
			print ("turning off green LED")
			turnOff(greenPin)

def turnOn(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
