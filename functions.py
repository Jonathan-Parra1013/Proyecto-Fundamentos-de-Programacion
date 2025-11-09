from flask import Flask, render_template, request
from functions import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

# Información de los integrantes
INTEGRANTES = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET"])
def index():
    equipos = obtener_equipos()
    equipos_info = []

    for equipo in equipos:
        logo = obtener_logo_equipo(equipo)
        equipos_info.append({"nombre": equipo, "logo": logo})

    equipo_seleccionado = request.args.get("equipo")
    jugadores = None
    if equipo_seleccionado:
        jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        equipos_info=equipos_info,
        jugadores=jugadores,
        equipo_seleccionado=equipo_seleccionado,
        integrantes=INTEGRANTES
    )

if __name__ == "__main__":
    app.run(debug=True)
