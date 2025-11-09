from flask import Flask, render_template, request
from functions import obtener_equipos, obtener_jugadores_por_equipo, comparar_jugadores, graficar_comparacion, mapa_calor

app = Flask(__name__)

# Integrantes del proyecto
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos()
    seleccionados = []
    comparacion_img = None
    mapa_img = None

    if request.method == "POST":
        jugadores_seleccionados = request.form.getlist("jugadores")
        if jugadores_seleccionados:
            comp_df = comparar_jugadores(jugadores_seleccionados)
            comparacion_img = graficar_comparacion(comp_df)
            mapa_img = mapa_calor(comp_df)

    return render_template(
        "index.html",
        equipos=equipos,
        integrantes=integrantes,
        comparacion_img=comparacion_img,
        mapa_img=mapa_img
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
