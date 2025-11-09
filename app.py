from flask import Flask, render_template, request
from functions import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    equipos_nombres = obtener_equipos()
    equipo_seleccionado = None
    jugadores = []
    logo_equipo = None

    if request.method == "POST":
        equipo_seleccionado = request.form.get("equipo")
        jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
        logo_equipo = obtener_logo_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        equipos=equipos_nombres,
        equipo_seleccionado=equipo_seleccionado,
        jugadores=jugadores,
        logo_equipo=logo_equipo,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
