import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import base64


EXCEL_FILE = "TABLAPREMIER.xlsx"  
df = pd.read_excel(EXCEL_FILE, sheet_name="Hoja1")


LOGOS_PATH = "static/logos"


def obtener_equipos():
    return sorted(df["EQUIPO"].dropna().unique().tolist())


def obtener_jugadores_por_equipo(equipo):
    jugadores = df[df["EQUIPO"] == equipo]["Nombre"].dropna().tolist()
    return jugadores


def obtener_logo_equipo(equipo):
    try:
        for ext in [".png", ".jpg", ".jpeg", ".webp"]:
            path = os.path.join(LOGOS_PATH, f"{equipo}{ext}")
            if os.path.exists(path):
                return f"/{path}"  
        return "/static/logos/default.png"  
    except Exception:
        return "/static/logos/default.png"


def comparar_jugadores(lista_jugadores):
    seleccion = df[df["Nombre"].isin(lista_jugadores)]
    if seleccion.empty:
        return {"error": "No se encontraron jugadores seleccionados"}

   
    fig, ax = plt.subplots(figsize=(8, 5))
    seleccion.plot(x="Nombre", y=["Goles", "Asistencias", "Tiros a puerta"], kind="bar", ax=ax)
    plt.title("Comparación de Rendimiento entre Jugadores")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=30)
    plt.tight_layout()

   
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    grafico_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    
    stats = seleccion[["Goles", "Asistencias", "Tiros a puerta", "Atajadas", "TA", "TR"]].corr()
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    sns.heatmap(stats, annot=True, cmap="YlGnBu", ax=ax2)
    plt.title("Mapa de Calor de Estadísticas")
    plt.tight_layout()

    buf2 = io.BytesIO()
    plt.savefig(buf2, format="png")
    buf2.seek(0)
    mapa_base64 = base64.b64encode(buf2.read()).decode("utf-8")
    plt.close(fig2)

    return {
        "jugadores": lista_jugadores,
        "grafico": grafico_base64,
        "mapa_calor": mapa_base64
    }

