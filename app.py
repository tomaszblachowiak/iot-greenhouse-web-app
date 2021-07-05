from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/charts/')
def charts():
    return render_template("charts.html")

@app.route('/howitworks/')
def howitworks():
    return "How it works page."

if __name__=="__main__":
    app.run(debug=True)