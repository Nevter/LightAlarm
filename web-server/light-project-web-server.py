import sys
sys.path.insert(0, './backend/')

import device
import alarm
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello():
   return render_template('main.html')

@app.route("/setLED/<brightness>/<colour>")
def setLED(colour, brightness):
    device.setLED(colour, brightness)
    return redirect("/")

@app.route("/setAlarm/<hours>/<minutes>")
def setAlarm(hours, minutes):
    alarm.setAlarm(hours, minutes)
    return redirect("/")


if (__name__) == ("__main__"):
   app.run(host='0.0.0.0', port=5000, debug=True)
