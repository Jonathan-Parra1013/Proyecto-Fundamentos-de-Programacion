from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores

app = Flask(__name__)

# Lista de integrantes
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

# Lista de equipos
equipos = obtener_equipos()  # Lista de equipos para el select

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        equipo_seleccionado = request.form.get('equipo')
        resultado = obtener_jugadores(equipo_seleccionado)
    return render_template('index.html', integrantes=integrantes, equipos=equipos, resultado=resultado)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


