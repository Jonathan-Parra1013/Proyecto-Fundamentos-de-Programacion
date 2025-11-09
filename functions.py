import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta del Excel
EXCEL_FILE = "TABLAPREMIER.xlsx"

# Cargar hoja de jugadores (Hoja2)
df = pd.read_excel(EXCEL_FILE, sheet_name="Hoja2")

# Normalizar nombres de columnas: quitar espacios y pasar a mayúsculas
df.columns = [col.strip().upper() for col in df.columns]

# Columnas importantes
col_equipo = "EQUIPO"
col_jugador = "NOMBRE"

# Funciones principales
def obtener_equipos():
    return sorted(df[col_equipo].dropna().unique().tolist())

def obtener_jugadores_por_equipo(equipo):
    jugadores = df[df[col_equipo] == equipo][col_jugador].dropna().tolist()
    return jugadores

def obtener_datos_jugador(nombre):
    fila = df[df[col_jugador] == nombre]
    if fila.empty:
        return None
    return fila.iloc[0].to_dict()

# Comparar jugadores seleccionados
def comparar_jugadores(jugadores_seleccionados):
    datos = [obtener_datos_jugador(j) for j in jugadores_seleccionados]
    comp_df = pd.DataFrame(datos)
    return comp_df

# Graficar barras comparativas
def graficar_comparacion(comp_df, columnas=None):
    if columnas is None:
        columnas = ["EDAD","TA","TR","ASISTENCIAS","TIROS A PUERTA",
                    "TOTAL DE TIROS","TOTAL DE GOLES","GOLES","ATAJADAS"]
    
    comp_df.set_index(col_jugador, inplace=True)
    comp_df[columnas].plot(kind="bar", figsize=(12,6))
    plt.tight_layout()
    img_path = "static/comparacion.png"
    plt.savefig(img_path)
    plt.close()
    return img_path

# Generar mapas de calor
def mapa_calor(comp_df, columnas=None):
    if columnas is None:
        columnas = ["EDAD","TA","TR","ASISTENCIAS","TIROS A PUERTA",
                    "TOTAL DE TIROS","TOTAL DE GOLES","GOLES","ATAJADAS"]
    
    comp_df.set_index(col_jugador, inplace=True)
    plt.figure(figsize=(10,6))
    sns.heatmap(comp_df[columnas], annot=True, cmap="YlGnBu")
    plt.tight_layout()
    img_path = "static/mapa_calor.png"
    plt.savefig(img_path)
    plt.close()
    return img_path
