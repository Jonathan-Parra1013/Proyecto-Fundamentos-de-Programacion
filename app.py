from flask import Flask, render_template, request
import os
from functions import obtener_equipos_con_logos, obtener_jugadores_por_equipo, comparar_jugadores, graficar_comparacion, mapa_calor

# Asegurarse de que Flask encuentra la carpeta static
app = Flask(__name__, static_folder=os.path.abspath('static'))
print(f"Carpeta static configurada en: {app.static_folder}")

# Integrantes del grupo
integrantes = [
    "Galeano Vargas Juan Enriquen",
    "Granja Espinosa David Santiago",
    "Muñoz Cubides Carol Daniela",
    "Parra Landinez Jonathan"
]

@app.route("/", methods=["GET", "POST"])
def index():
    equipos = obtener_equipos_con_logos()
    comparacion_img = None
    mapa_img = None
    jugadores_por_equipo = {}

    # Guardar jugadores de cada equipo para JS
    for equipo in equipos:
        jugadores_por_equipo[equipo["Equipo"]] = obtener_jugadores_por_equipo(equipo["Equipo"])

    if request.method == "POST":
        jugadores_seleccionados = request.form.getlist("jugadores")
        if jugadores_seleccionados:
            try:
                print("Jugadores seleccionados:", jugadores_seleccionados)
                imagenes = comparar_jugadores(jugadores_seleccionados)
                print("Visualizaciones generadas exitosamente")
                return render_template(
                    "index.html",
                    equipos=equipos,
                    integrantes=integrantes,
                    jugadores_por_equipo=jugadores_por_equipo,
                    comparacion_img=imagenes['comparacion'],
                    mapa_img=imagenes['mapa_calor'],
                    radar_img=imagenes['radar'],
                    ranking_img=imagenes['ranking'],
                    percentiles_img=imagenes['percentiles']
                )
            except Exception as e:
                print("Error al procesar jugadores:", str(e))
                return f"Error: {str(e)}", 500

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
