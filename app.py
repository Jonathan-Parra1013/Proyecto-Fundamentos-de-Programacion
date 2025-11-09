from flask import Flask, render_template, request
from main import obtener_equipos, obtener_jugadores

app = Flask(__name__)

# Lista de tuplas: (nombre del equipo, nombre del archivo del logo)
equipos = obtener_equipos()  
equipos_dict = {nombre: logo for nombre, logo in equipos}  # Para mostrar el logo grande del equipo seleccionado

# Integrantes
integrantes = [
    "Galeano Vargas Juan Enriquen", 
    "Granja Espinosa David Santiago", 
    "Muñoz Cubides Carol Daniela", 
    "Parra Landinez Jonathan"
]

@app.route('/', methods=['GET'])
def index():
    equipo_seleccionado = request.args.get('equipo')
    resultado = None
    if equipo_seleccionado:
        resultado = obtener_jugadores(equipo_seleccionado)
    return render_template(
        'index.html', 
        equipos=equipos, 
        equipos_dict=equipos_dict, 
        resultado=resultado, 
        equipo_seleccionado=equipo_seleccionado,
        integrantes=integrantes
    )

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
