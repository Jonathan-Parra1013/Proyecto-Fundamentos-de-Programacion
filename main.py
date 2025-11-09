import pandas as pd
import os

# Ruta correcta al archivo Excel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(BASE_DIR, "data", "TABLAPREMIER.xlsx")

# --- Detectar automáticamente los nombres de las hojas ---
xlsx = pd.ExcelFile(excel_path)
print("Hojas detectadas:", xlsx.sheet_names)  # útil para depuración en local

# Buscar la hoja de logos (la que tenga columna "EQUIPO" y "LOGO")
for sheet in xlsx.sheet_names:
    df_temp = pd.read_excel(excel_path, sheet_name=sheet)
    if "LOGO" in df_temp.columns and "EQUIPO" in df_temp.columns:
        df_logos = df_temp
    elif "EQUIPO" in df_temp.columns and "NOMBRE" in df_temp.columns:
        df_jugadores = df_temp

# Función: obtener todos los equipos
def obtener_equipos():
    equipos = df_logos["EQUIPO"].dropna().tolist()
    return equipos

# Función: obtener jugadores por equipo
def obtener_jugadores_por_equipo(equipo):
    jugadores = df_jugadores[df_jugadores["EQUIPO"] == equipo]
    if jugadores.empty:
        return "<p>No hay jugadores para este equipo.</p>"
    tabla_html = jugadores.to_html(index=False, classes="jugadores-tabla")
    return tabla_html

# Función: obtener logo de un equipo
def obtener_logo_equipo(equipo):
    fila = df_logos[df_logos["EQUIPO"] == equipo]
    if not fila.empty:
        return f"/static/logos/{fila['LOGO'].values[0]}"
    return None
