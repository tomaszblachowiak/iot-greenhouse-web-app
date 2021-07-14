from flask import Flask, render_template
import json
from urllib.request import urlopen
from datetime import datetime


app=Flask(__name__)

@app.route('/')
def home():
    response = urlopen('https://hydropoinc-greenhouse-api.azurewebsites.net/api/readings/GetAllReadings?')
    data_json = json.loads(response.read())
    temperature1 = [d["temperature1"] for d in data_json if "temperature1" in d]
    temperature2 = [d["temperature2"] for d in data_json if "temperature2" in d]
    temperature3 = [float(d["temperature1"])-2.0 for d in data_json if "temperature1" in d]
    humidity = [d["humidity1"] for d in data_json if "humidity1" in d]
    pressure = [d["pressure1"] for d in data_json if "pressure1" in d]
    ts = [datetime.fromtimestamp(int(d['_ts'])).isoformat(timespec='minutes') for d in data_json if '_ts' in d]
    #print(temperature1)
    #print(ts)
    return render_template("home.html", temperature1 = temperature1, temperature2 = temperature2, temperature3 = temperature3, humidity = humidity, pressure = pressure, ts = ts)

@app.route('/charts/')
def charts():
    return render_template("charts.html")

@app.route('/howitworks/')
def howitworks():
    return "How it works page."

if __name__=="__main__":
    app.run(debug=True)