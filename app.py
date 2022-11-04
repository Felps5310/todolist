from flask import Flask

app  = Flask(__name__)

@app.route("/")
def home():
    return "<html><body>Hello World</body></html>"
@app.route("/bye")
def bye():
    return "Bye"

app.run(debug=True)
