from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello and welcome at homepage!"

@app.route('/howitworks/')
def howitworks():
    return "How it works page."

if __name__=="__main__":
    app.run(debug=True)