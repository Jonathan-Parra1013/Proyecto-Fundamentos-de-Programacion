from flask import Flask, render_template, request
from functions import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

# Integrantes tal como pediste
INTEGRANTES = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos()  # lista de dicts {"nombre","logo"}
    equipo_seleccionado = None
    jugadores = []
    logo_equipo = None

    # usamos POST cuando el usuario hace clic en un logo (botón)
    if request.method == "POST":
        equipo_seleccionado = request.form.get("equipo")
        if equipo_seleccionado:
            jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
            logo_equipo = obtener_logo_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        equipos=equipos,
        equipo_seleccionado=equipo_seleccionado,
        jugadores=jugadores,
        logo_equipo=logo_equipo,
        integrantes=INTEGRANTES
    )

if __name__ == "__main__":
    # Render usa PORT env; local usa 5000
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
