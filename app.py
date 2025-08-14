from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicación Flask OK 👍UNIVERSIDAD ESTATAL  AMAZONICA "

@app.route("/usuario/")
@app.route("/usuario/<nombre>")
def usuario(nombre="Edilson"):
    return f"Bienvenido, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)
