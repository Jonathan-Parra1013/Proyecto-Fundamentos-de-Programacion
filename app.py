from flask import Flask, render_template, request
from main import obtener_jugadores  # importas tu función principal

app = Flask(__name__)

equipos = obtener_jugadores.obtener_equipos()  # función que devuelve la lista de equipos

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        equipo_seleccionado = request.form.get('equipo')
        resultado = obtener_jugadores(jugador_equipo=equipo_seleccionado)
    return render_template('index.html', equipos=equipos, resultado=resultado)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


