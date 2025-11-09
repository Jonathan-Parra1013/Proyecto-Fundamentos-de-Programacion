from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos()
    jugadores = None
    logo_equipo = None
    equipo_seleccionado = None

    if request.method == "POST":
        equipo_seleccionado = request.form["equipo"]
        jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
        logo_equipo = obtener_logo_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        equipos=equipos,
        jugadores=jugadores,
        logo_equipo=logo_equipo,
        equipo_seleccionado=equipo_seleccionado,
        integrantes=[
            "Jonathan Parra Landinez",
            "Juan Sebastián Gómez",
            "Valentina Rojas",
            "Camilo Andrés Pérez"
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)
