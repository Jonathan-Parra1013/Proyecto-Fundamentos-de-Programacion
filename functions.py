import pandas as pd
import os

# Ruta del archivo Excel (ajusta si lo pusiste en otra carpeta)
excel_path = os.path.join("data", "TABLAPREMIER.xlsx")

# Cargar hojas (Hoja1 = logos / Hoja2 = jugadores)
df_equipos = pd.read_excel(excel_path, sheet_name="Hoja1")
df_jugadores = pd.read_excel(excel_path, sheet_name="Hoja2")

# Normalizar nombres de columnas (quita espacios al inicio/fin)
df_equipos.columns = [c.strip() for c in df_equipos.columns]
df_jugadores.columns = [c.strip() for c in df_jugadores.columns]

def obtener_equipos():
    """Devuelve lista de dicts {nombre, logo} desde Hoja1"""
    equipos = []
    # Asume columnas: EQUIPO, LOGO (tal cual en Hoja1)
    for _, fila in df_equipos.iterrows():
        nombre = fila.get("EQUIPO") or fila.get("Equipo")  # tolerancia
        logo = fila.get("LOGO") or fila.get("Logo")
        if pd.notna(nombre):
            equipos.append({
                "nombre": str(nombre),
                "logo": str(logo) if pd.notna(logo) else None
            })
    return equipos

def obtener_logo_equipo(equipo):
    fila = df_equipos[df_equipos["EQUIPO"] == equipo] if "EQUIPO" in df_equipos.columns else df_equipos[df_equipos["Equipo"] == equipo]
    if not fila.empty:
        if "LOGO" in fila.columns:
            return fila.iloc[0]["LOGO"]
        if "Logo" in fila.columns:
            return fila.iloc[0]["Logo"]
    return None

def obtener_jugadores_por_equipo(equipo):
    # Asume en Hoja2 columna llamada "EQUIPO" o "Equipo"
    if "EQUIPO" in df_jugadores.columns:
        jugadores = df_jugadores[df_jugadores["EQUIPO"] == equipo]
    else:
        jugadores = df_jugadores[df_jugadores["Equipo"] == equipo]
    # Devuelve lista de dicts; convierte NaN a cadena vacía
    registros = jugadores.fillna("").to_dict(orient="records")
    return registros
