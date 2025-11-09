import pandas as pd

# Ruta del archivo Excel
excel_path = "data/TABLAPREMIER.xlsx"

# Leer las hojas del Excel
df_logos = pd.read_excel(excel_path, sheet_name="hoja1")
df_jugadores = pd.read_excel(excel_path, sheet_name="hoja2")

# --- FUNCIONES ---

def obtener_equipos():
    """Devuelve la lista de equipos únicos."""
    equipos = df_logos["Equipo"].dropna().unique().tolist()
    return equipos

def obtener_logo_equipo(equipo_nombre):
    """Devuelve el logo del equipo seleccionado."""
    fila = df_logos[df_logos["Equipo"] == equipo_nombre]
    if not fila.empty:
        return fila.iloc[0]["Logo"]
    return None

def obtener_jugadores_por_equipo(equipo_nombre):
    """Devuelve la lista de jugadores del equipo seleccionado."""
    jugadores = df_jugadores[df_jugadores["Equipo"] == equipo_nombre]["Jugador"].dropna().tolist()
    return jugadores
