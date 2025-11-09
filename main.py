import pandas as pd

# Leer logos de la hoja1
df_logos = pd.read_excel("datos.xlsx", sheet_name="hoja1")
# Crear lista de tuplas (nombre_equipo, logo)
equipos = [(row["Equipo"], row["Logo"]) for _, row in df_logos.iterrows()]

# Leer jugadores de la hoja2
df_jugadores = pd.read_excel("datos.xlsx", sheet_name="hoja2")

def obtener_equipos():
    """Devuelve lista de tuplas (nombre_equipo, logo)"""
    return equipos

def obtener_jugadores_por_equipo(nombre_equipo):
    """Devuelve lista de jugadores de un equipo"""
    jugadores = df_jugadores[df_jugadores["Equipo"] == nombre_equipo]
    return [row["Nombre"] for _, row in jugadores.iterrows()]
