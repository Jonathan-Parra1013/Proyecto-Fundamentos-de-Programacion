from flask import Flask, render_template, request, jsonify
from functions import (
    obtener_equipos,
    obtener_jugadores_por_equipo,
    obtener_logo_equipo,
    comparar_jugadores
)
import os

app = Flask(__name__)

# 🔹 Integrantes del proyecto
INTEGRANTES = [
    "Galeano Vargas Juan Enrique",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

# 🔹 Página principal
@app.route("/")
def index():
    equipos = obtener_equipos()
    return render_template("index.html", equipos=equipos, integrantes=INTEGRANTES)

# 🔹 Obtener jugadores por equipo (AJAX)
@app.route("/jugadores/<equipo>")
def jugadores_por_equipo(equipo):
    jugadores = obtener_jugadores_por_equipo(equipo)
    logo = obtener_logo_equipo(equipo)
    return jsonify({"jugadores": jugadores, "logo": logo})

# 🔹 Comparar jugadores seleccionados
@app.route("/comparar", methods=["POST"])
def comparar():
    jugadores = request.json.get("jugadores", [])
    resultados = comparar_jugadores(jugadores)
    return jsonify(resultados)

# 🔹 Configuración para Render (port binding)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port, debug=False)
