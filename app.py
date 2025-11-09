from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores_por_equipo

app = Flask(__name__)

equipos = obtener_equipos()  # Lista de tuplas (nombre, logo)

# Integrantes
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    equipo_seleccionado = None
    if request.method == 'POST':
        equipo_seleccionado = request.form.get('equipo')
        if equipo_seleccionado:
            jugadores = obtener_jugadores_por_equipo(equipo_seleccionado)
            # Crear lista en HTML
            resultado = "<ul>"
            for j in jugadores:
                resultado += f"<li>{j}</li>"
            resultado += "</ul>"

    return render_template(
        'index.html',
        equipos=equipos,
        resultado=resultado,
        equipo_seleccionado=equipo_seleccionado,
        integrantes=integrantes
    )

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
