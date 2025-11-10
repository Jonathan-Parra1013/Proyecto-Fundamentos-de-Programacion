import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from models.jugador import Jugador
from models.analizador import AnalizadorEstadisticas


EXCEL_FILE = "TABLAPREMIER.xlsx"


df_equipos = pd.read_excel(EXCEL_FILE, sheet_name="Hoja1")
df_jugadores = pd.read_excel(EXCEL_FILE, sheet_name="Hoja2")


analizador = AnalizadorEstadisticas(df_jugadores)


col_equipo_jugadores = None
col_nombre_jugador = None
for col in df_jugadores.columns:
    if col.strip().upper() == "EQUIPO":
        col_equipo_jugadores = col
    if col.strip().upper() == "NOMBRE":
        col_nombre_jugador = col

if col_equipo_jugadores is None or col_nombre_jugador is None:
    raise ValueError("No se encontró la columna 'EQUIPO' o 'NOMBRE' en Hoja2")


def obtener_equipos_con_logos():
    return df_equipos[["Equipo", "LOGO"]].dropna().to_dict(orient="records")


def obtener_jugadores_por_equipo(equipo):
    jugadores = df_jugadores[df_jugadores[col_equipo_jugadores] == equipo][col_nombre_jugador].dropna().tolist()
    return jugadores


def obtener_datos_jugador(nombre):
    fila = df_jugadores[df_jugadores[col_nombre_jugador] == nombre]
    if fila.empty:
        print(f"No se encontraron datos para el jugador: {nombre}")
        return None
    
    datos = fila.iloc[0].to_dict()
   
    datos['Nombre'] = nombre
    return datos


def comparar_jugadores(jugadores_seleccionados):
    datos = []
    for jugador in jugadores_seleccionados:
        datos_jugador = obtener_datos_jugador(jugador)
        if datos_jugador is not None:
            datos.append(datos_jugador)
        else:
            raise ValueError(f"No se encontraron datos para el jugador: {jugador}")
    
    if not datos:
        raise ValueError("No se pudieron obtener datos para ningún jugador")
    
    comp_df = pd.DataFrame(datos)
    
    
    columnas_numericas = ["Edad", "TA", "TR", "Asistencias", "Tiros a puerta", 
                         "Total de tiros", "Total de goles", "Goles", "Atajadas"]
    
    for col in columnas_numericas:
        if col in comp_df.columns:
            comp_df[col] = pd.to_numeric(comp_df[col], errors='coerce')
    
   
    for col in columnas_numericas:
        if col in comp_df.columns:
            comp_df[col] = pd.to_numeric(comp_df[col], errors='coerce')

    
    imagenes = {}
    try:
       
        imagenes['comparacion'] = graficar_comparacion(comp_df.copy())
        
      
        imagenes['mapa_calor'] = mapa_calor(comp_df.copy())
        
        return imagenes
    except Exception as e:
        raise ValueError(f"Error al generar las visualizaciones: {str(e)}")


def graficar_comparacion(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    columnas_disponibles = [col for col in columnas if col in comp_df.columns]
    if not columnas_disponibles:
        raise ValueError("No hay columnas válidas para graficar")
    
    try:
        comp_df.set_index('Nombre', inplace=True)
        ax = comp_df[columnas_disponibles].plot(kind="bar", figsize=(12,6), colormap="viridis")
            plt.title("Comparación de Estadísticas de Jugadores")
        plt.xlabel("Jugadores")
        plt.ylabel("Valores")
        plt.xticks(rotation=45)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
           
            plt.figtext(0.05, -0.1, 
                "Este gráfico muestra una comparación directa de las estadísticas clave entre los jugadores seleccionados.\n" +
                "Las barras representan los valores numéricos para cada estadística, permitiendo una comparación visual rápida.\n" +
                "Mayor altura de la barra indica mejor rendimiento en esa categoría.",
                wrap=True, horizontalalignment='left', fontsize=8)
        
        plt.tight_layout()
        
        
        os.makedirs("static", exist_ok=True)
        img_path = "static/comparacion.png"
        plt.savefig(img_path, bbox_inches='tight', dpi=300)
        plt.close()
        return img_path
    except Exception as e:
        plt.close()  
        raise ValueError(f"Error al crear el gráfico de comparación: {str(e)}")


def mapa_calor(comp_df, columnas=None):
    if columnas is None:
        columnas = ["Edad","TA","TR","Asistencias","Tiros a puerta","Total de tiros","Total de goles","Goles","Atajadas"]
    
    
    columnas_disponibles = [col for col in columnas if col in comp_df.columns]
    if not columnas_disponibles:
        raise ValueError("No hay columnas válidas para el mapa de calor")
    
    try:
        comp_df.set_index('Nombre', inplace=True)
        plt.figure(figsize=(12,6))
        sns.heatmap(comp_df[columnas_disponibles], annot=True, cmap="YlGnBu", cbar=True, fmt='.1f')
        plt.title("Mapa de Calor - Comparación de Jugadores")
        plt.xlabel("Estadísticas")
        plt.ylabel("Jugadores")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        
        os.makedirs("static", exist_ok=True)
        img_path = "static/mapa_calor.png"
        plt.savefig(img_path, bbox_inches='tight', dpi=300)
        plt.close()
        return img_path
    except Exception as e:
        plt.close()  
        raise ValueError(f"Error al crear el mapa de calor: {str(e)}")
