from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores_por_equipo, obtener_logo_equipo

app = Flask(__name__)

# Integrantes del grupo
integrantes = [
    "Galeano Vargas Juan Enrique",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos()
    equipo_seleccionado = None
    resultado = None
    logo_equipo = None

    if request.method == "POST":
        equipo_seleccionado = request.form.get("equipo")
        resultado = obtener_jugadores_por_equipo(equipo_seleccionado)
        logo_equipo = obtener_logo_equipo(equipo_seleccionado)

    return render_template(
        "index.html",
        equipos=equipos,
        integrantes=integrantes,
        resultado=resultado,
        equipo_seleccionado=equipo_seleccionado,
        logo_equipo=logo_equipo
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
