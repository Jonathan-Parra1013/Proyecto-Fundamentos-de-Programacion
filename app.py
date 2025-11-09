from flask import Flask, render_template, request
from functions import obtener_equipos_con_logos, obtener_jugadores_por_equipo, comparar_jugadores, graficar_comparacion, mapa_calor

app = Flask(__name__)

# Integrantes
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos_con_logos()
    seleccionados = []
    comparacion_img = None
    mapa_img = None
    jugadores_por_equipo = {}

    # Guardar jugadores de cada equipo para JS
    for equipo in equipos:
        jugadores_por_equipo[equipo["Equipo"]] = obtener_jugadores_por_equipo(equipo["Equipo"])

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
        jugadores_por_equipo=jugadores_por_equipo,
        comparacion_img=comparacion_img,
        mapa_img=mapa_img
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
