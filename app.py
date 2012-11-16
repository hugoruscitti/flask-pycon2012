import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "Bienvenidos!!!"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "Hola <b>{nombre}</b> como estas?".format(nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
