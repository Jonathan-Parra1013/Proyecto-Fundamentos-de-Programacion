from flask import Flask, render_template, request
from functions import (
    obtener_equipos,
    obtener_jugadores_por_equipo,
    obtener_datos_jugadores,
    generar_grafica_comparacion,
    generar_mapa_calor
)

app = Flask(__name__)


INTEGRANTES = [
    "Galeano Vargas Juan Enrique",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]


@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos()
    jugadores = []
    seleccionados = []
    grafica = None
    mapa = None

    if request.method == "POST":
        equipo = request.form.get("equipo")
        nombres = request.form.getlist("jugadores")

        if nombres:
            # Obtener los datos de los jugadores seleccionados
            df_jugadores = obtener_datos_jugadores(nombres)
            grafica = generar_grafica_comparacion(df_jugadores)
            mapa = generar_mapa_calor(df_jugadores)
            seleccionados = nombres
        elif equipo:
            # Mostrar jugadores del equipo seleccionado
            jugadores = obtener_jugadores_por_equipo(equipo)

    return render_template(
        "index.html",
        equipos=equipos,
        jugadores=jugadores,
        seleccionados=seleccionados,
        grafica=grafica,
        mapa=mapa,
        integrantes=INTEGRANTES  
    )

if __name__ == "__main__":
    app.run(debug=True)
