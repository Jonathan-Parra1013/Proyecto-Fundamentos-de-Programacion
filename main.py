import pandas as pd
import os

# Ruta del archivo Excel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_excel = os.path.join(BASE_DIR, "data", "TABLAPREMIER.xlsx")

# Cargamos las dos hojas (asegúrate que las hojas se llamen "Hoja1" y "Hoja2")
df_logos = pd.read_excel(ruta_excel, sheet_name="Hoja1")
df_datos = pd.read_excel(ruta_excel, sheet_name="Hoja2")

def obtener_equipos():
    """Devuelve lista de equipos únicos (ordenada por aparición)."""
    equipos = df_logos["EQUIPO"].dropna().unique().tolist()
    return equipos

def obtener_jugadores_por_equipo(equipo):
    """Devuelve DataFrame con jugadores del equipo (puede ser vacío)."""
    jugadores = df_datos[df_datos["EQUIPO"] == equipo]
    return jugadores

def obtener_logo_equipo(equipo):
    """Devuelve el nombre de archivo del logo para el equipo (ej: 'liverpool.png')."""
    fila = df_logos[df_logos["EQUIPO"] == equipo]
    if not fila.empty:
        return fila["LOGO"].values[0]
    return None
