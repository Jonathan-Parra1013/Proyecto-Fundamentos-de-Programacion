import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta del Excel
EXCEL_FILE = "TABLAPREMIER.xlsx"

# Cargar hoja principal (Hoja1)
df = pd.read_excel(EXCEL_FILE, sheet_name="Hoja1")

# Detectar automáticamente columna de equipo
col_equipo = None
for col in df.columns:
    if col.strip().upper() == "EQUIPO":
        col_equipo = col
        break

if col_equipo is None:
    raise ValueError("No se encontró la columna 'EQUIPO' en el Excel")

# Funciones principales
def obtener_equipos():
    return sorted(df[col_equipo].dropna().unique().tolist())

def obtener_jugadores_por_equipo(equipo):
    jugadores = df[df[col_equipo] == equipo]["Nombre"].dropna().tolist()
    return jugadores

def obtener_datos_jugador(nombre):
    fila = df[df["Nombre"] == nombre]
    if fila.empty:
        return None
    return fila.iloc[0].to_dict()

# Función para comparar jugadores seleccionados
def comparar_jugadores(jugadores_seleccionados):
    datos = [obtener_datos_jugador(j) for j in jugadores_seleccionados]
    comp_df = pd.DataFrame(datos)
    return comp_df

# Graficar barras comparativas
def graficar_comparacion(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    comp_df.set_index("Nombre", inplace=True)
    comp_df[columnas].plot(kind="bar", figsize=(12,6))
    plt.tight_layout()
    img_path = "static/comparacion.png"
    plt.savefig(img_path)
    plt.close()
    return img_path

# Generar mapas de calor
def mapa_calor(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    comp_df.set_index("Nombre", inplace=True)
    plt.figure(figsize=(10,6))
    sns.heatmap(comp_df[columnas], annot=True, cmap="YlGnBu")
    plt.tight_layout()
    img_path = "static/mapa_calor.png"
    plt.savefig(img_path)
    plt.close()
    return img_path
