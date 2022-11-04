from flask import Flask, render_template

app  = Flask(__name__)

@app.route("/")
def home():
    #templates/home
    return render_templates(home.html)
@app.route("/bye")
def bye():
    return "Bye"

app.run(debug=True)
