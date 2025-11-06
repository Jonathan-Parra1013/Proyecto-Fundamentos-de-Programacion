# main.py
import pandas as pd

# Ruta del archivo Excel
ARCHIVO_EXCEL = 'data/TABLAPREMIER.xlsx'
SHEET_NAME = 'Hoja2'

def cargar_datos():
    try:
        df = pd.read_excel(ARCHIVO_EXCEL, sheet_name=SHEET_NAME)
        return df
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return pd.DataFrame() 

def obtener_equipos():
    
    df = cargar_datos()
    if not df.empty:
        return sorted(df['Equipo'].unique())
    return []

def obtener_jugadores(equipo):
  
    df = cargar_datos()
    if df.empty:
        return "La base de datos no se pudo cargar."

    # Filtrar jugadores del equipo seleccionado
    jugadores = df[df['Equipo'].str.lower() == equipo.lower()]
    
    if len(jugadores) > 0:
        # Devuelve HTML listo para mostrar en la web
        return jugadores.to_html(classes='tabla', index=False)
    else:
        return "No se encontraron jugadores para este equipo."
