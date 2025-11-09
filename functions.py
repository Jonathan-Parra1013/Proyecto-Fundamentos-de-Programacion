import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Archivos Excel
EXCEL_FILE = "TABLAPREMIER.xlsx"

# Cargar hojas
df_equipos = pd.read_excel(EXCEL_FILE, sheet_name="Hoja1")
df_jugadores = pd.read_excel(EXCEL_FILE, sheet_name="Hoja2")

# Detectar columnas
col_equipo_jugadores = None
col_nombre_jugador = None
for col in df_jugadores.columns:
    if col.strip().upper() == "EQUIPO":
        col_equipo_jugadores = col
    if col.strip().upper() == "NOMBRE":
        col_nombre_jugador = col

if col_equipo_jugadores is None or col_nombre_jugador is None:
    raise ValueError("No se encontró la columna 'EQUIPO' o 'NOMBRE' en Hoja2")

# Función: obtener equipos con logos
def obtener_equipos_con_logos():
    return df_equipos[["Equipo", "LOGO"]].dropna().to_dict(orient="records")

# Función: jugadores por equipo
def obtener_jugadores_por_equipo(equipo):
    jugadores = df_jugadores[df_jugadores[col_equipo_jugadores] == equipo][col_nombre_jugador].dropna().tolist()
    return jugadores

# Datos de un jugador
def obtener_datos_jugador(nombre):
    fila = df_jugadores[df_jugadores[col_nombre_jugador] == nombre]
    if fila.empty:
        return None
    return fila.iloc[0].to_dict()

# Comparar jugadores seleccionados
def comparar_jugadores(jugadores_seleccionados):
    datos = [obtener_datos_jugador(j) for j in jugadores_seleccionados]
    comp_df = pd.DataFrame(datos)
    return comp_df

# Graficar comparación
def graficar_comparacion(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    comp_df.set_index(col_nombre_jugador, inplace=True)
    comp_df[columnas].plot(kind="bar", figsize=(12,6), colormap="viridis")
    plt.tight_layout()
    img_path = "static/comparacion.png"
    plt.savefig(img_path)
    plt.close()
    return img_path

# Mapa de calor
def mapa_calor(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    comp_df.set_index(col_nombre_jugador, inplace=True)
    plt.figure(figsize=(12,6))
    sns.heatmap(comp_df[columnas], annot=True, cmap="YlGnBu", cbar=True)
    plt.tight_layout()
    img_path = "static/mapa_calor.png"
    plt.savefig(img_path)
    plt.close()
    return img_path
