from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    equipos_nombres = obtener_equipos()
    equipo_seleccionado = None
    jugadores = []
    logo = None

    if request.method == "POST":
        equipo_seleccionado = request.form.get("equipo")
        jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
        logo = obtener_logo_equipo(equipo_seleccionado)

    # Integrantes del grupo (completos)
    integrantes = [
        "Jonathan Parra Landinez",
        "Sebastián Rojas Peña",
        "Juan José Rivera Méndez",
        "Andrés Felipe Martínez Sánchez"
    ]

    return render_template(
        "index.html",
        equipos=equipos_nombres,
        equipo=equipo_seleccionado,
        jugadores=jugadores,
        logo=logo,
        integrantes=integrantes
    )

if __name__ == "__main__":
    app.run(debug=True)
