# api/index.py
from flask import Flask, render_template

# OJO: como este archivo vive en /api, indicamos rutas relativas a la raíz
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Bienvenido, {nombre}!"

@app.route("/health")
def health():
    return "ok"
