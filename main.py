import pandas as pd
import os

# Ruta al archivo Excel
excel_path = os.path.join(os.path.dirname(__file__), "TABLAPREMIER.xlsx")

# Cargar datos desde las hojas correctas
df = pd.read_excel(excel_path, sheet_name="Hoja2")   # Jugadores y estadísticas
df_logos = pd.read_excel(excel_path, sheet_name="Hoja1")  # Equipos y logos

# Asegurar que las columnas tengan nombres uniformes
df.columns = [col.strip() for col in df.columns]
df_logos.columns = [col.strip() for col in df_logos.columns]

def obtener_equipos():
    """Devuelve una lista de equipos únicos."""
    return sorted(df["Equipo"].dropna().unique())

def obtener_jugadores_por_equipo(equipo):
    """Filtra jugadores por nombre del equipo."""
    return df[df["Equipo"] == equipo][["Jugador", "Posición", "Goles", "Asistencias", "Edad"]]

def obtener_logo_equipo(equipo):
    """Obtiene la URL o ruta del logo del equipo."""
    fila = df_logos[df_logos["Equipo"] == equipo]
    if not fila.empty:
        return fila["Logo"].values[0]
    return None
