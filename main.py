import pandas as pd
import os

# Ruta correcta al archivo Excel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(BASE_DIR, "data", "TABLAPREMIER.xlsx")

# Leer las hojas
df_logos = pd.read_excel(excel_path, sheet_name="hoja1")
df_jugadores = pd.read_excel(excel_path, sheet_name="hoja2")

# Obtener lista de equipos y sus logos
def obtener_equipos():
    equipos = df_logos["EQUIPO"].tolist()
    return equipos

# Obtener jugadores por equipo
def obtener_jugadores_por_equipo(equipo):
    jugadores = df_jugadores[df_jugadores["EQUIPO"] == equipo]
    if jugadores.empty:
        return "<p>No hay jugadores para este equipo.</p>"
    
    tabla_html = jugadores.to_html(index=False, classes="jugadores-tabla")
    return tabla_html

# Obtener logo del equipo
def obtener_logo_equipo(equipo):
    fila = df_logos[df_logos["EQUIPO"] == equipo]
    if not fila.empty:
        return f"/static/logos/{fila['LOGO'].values[0]}"
    return None
