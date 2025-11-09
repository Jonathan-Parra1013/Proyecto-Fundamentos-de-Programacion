import pandas as pd
import os

# ===============================
# PROYECTO: Análisis de la Premier League
# INTEGRANTES:
# - Jonathan Parra Landinez
# - Cristian David Suarez
# - Mateo Hernández
# - Juan David Vargas
# - Luisa Fernanda Rodríguez
# ===============================

# Ruta del archivo Excel
excel_path = os.path.join("data", "TABLAPREMIER.xlsx")

# Cargar las hojas correctamente (respetando las mayúsculas del Excel)
df_logos = pd.read_excel(excel_path, sheet_name="Hoja1")
df_jugadores = pd.read_excel(excel_path, sheet_name="Hoja2")

# Función para obtener lista de equipos
def obtener_equipos():
    equipos = df_logos["Equipo"].dropna().unique().tolist()
    return equipos

# Función para obtener jugadores por equipo
def obtener_jugadores_por_equipo(equipo):
    jugadores = df_jugadores[df_jugadores["EQUIPO"] == equipo]
    return jugadores.to_dict(orient="records")

# Función para obtener logo del equipo
def obtener_logo_equipo(equipo):
    fila = df_logos[df_logos["Equipo"] == equipo]
    if not fila.empty:
        return fila.iloc[0]["LOGO"]
    return None
