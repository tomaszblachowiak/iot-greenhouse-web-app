from flask import Flask, render_template
import json
from urllib.request import urlopen

app=Flask(__name__)

@app.route('/')
def home():
    response = urlopen('https://hydropoinc-greenhouse-api.azurewebsites.net/api/readings/GetAllReadings?')
    data_json = json.loads(response.read())
    temperature1 = [d["temperature1"] for d in data_json if "temperature1" in d]
    ts = [d['_ts'] for d in data_json if '_ts' in d]
    print(temperature1)
    print(ts)
    return render_template("home.html", temperature1 = temperature1, ts = ts)

@app.route('/charts/')
def charts():
    return render_template("charts.html")

@app.route('/howitworks/')
def howitworks():
    return "How it works page."

if __name__=="__main__":
    app.run(debug=True)