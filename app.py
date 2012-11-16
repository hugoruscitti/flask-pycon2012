import flask
from flask import render_template
import helpers

app = flask.Flask(__name__)
helpers.load(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "Hola <b>{nombre}</b> como estas?".format(nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
