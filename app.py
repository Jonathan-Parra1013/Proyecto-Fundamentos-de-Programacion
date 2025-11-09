from flask import Flask, render_template, request, url_for
from main import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

# Integrantes (exactos que pediste)
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos_nombres = obtener_equipos()
    # Construimos lista de tuplas (nombre, logo_filename) para usar en template
    equipos = [(e, obtener_logo_equipo(e)) for e in equipos_nombres]

    equipo_seleccionado = None
    jugadores = None
    logo_filename = None

    if request.method == "POST":
        equipo_seleccionado = request.form.get("equipo")
        if equipo_seleccionado:
            jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
            logo_filename = obtener_logo_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        integrantes=integrantes,
        equipos=equipos,
        equipo_seleccionado=equipo_seleccionado,
        jugadores=jugadores,
        logo_filename=logo_filename
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

