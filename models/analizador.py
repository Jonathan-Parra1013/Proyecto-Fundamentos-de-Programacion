import pandas as pd
import numpy as np
from models.jugador import Jugador

class AnalizadorEstadisticas:
    def __init__(self, df_jugadores):
        self.df_jugadores = df_jugadores
    
    def calcular_percentiles(self, jugadores, columnas):
       
        datos = pd.DataFrame([j.obtener_estadisticas() for j in jugadores])
        percentiles = {}
        
        for col in columnas:
            if col in datos.columns:
                percentiles[col] = {}
                for nombre in datos['Nombre']:
                    valor = datos[datos['Nombre'] == nombre][col].iloc[0]
                    percentil = (datos[col] <= valor).mean() * 100
                    percentiles[col][nombre] = round(percentil, 2)
        
        return percentiles
    
    def generar_radar_chart_data(self, jugadores, metricas):
        """Genera datos para un gráfico de radar"""
        datos = pd.DataFrame([j.obtener_estadisticas() for j in jugadores])
        radar_data = {}
        
       
        for metrica in metricas:
            if metrica in datos.columns:
                min_val = datos[metrica].min()
                max_val = datos[metrica].max()
                if max_val > min_val:
                    datos[f"{metrica}_norm"] = (datos[metrica] - min_val) / (max_val - min_val)
                else:
                    datos[f"{metrica}_norm"] = 1
                
        
        for _, row in datos.iterrows():
            radar_data[row['Nombre']] = {
                metrica: row[f"{metrica}_norm"] 
                for metrica in metricas 
                if f"{metrica}_norm" in datos.columns
            }
        
        return radar_data
    
    def calcular_ranking(self, jugadores):
       
        datos = pd.DataFrame([j.obtener_estadisticas() for j in jugadores])
        
        
        pesos = {
            'Goles': 0.3,
            'Asistencias': 0.2,
            'Efectividad Tiros (%)': 0.15,
            'Efectividad Goles (%)': 0.15,
            'Tarjetas Rojas': -0.1,
            'Tarjetas Amarillas': -0.05,
            'Atajadas': 0.05
        }
        
       
        puntuacion = pd.Series(0, index=datos.index)
        for col, peso in pesos.items():
            if col in datos.columns:
                
                min_val = datos[col].min()
                max_val = datos[col].max()
                if max_val > min_val:
                    norm = (datos[col] - min_val) / (max_val - min_val)
                else:
                    norm = 1
                
                
                if col in ['Tarjetas Rojas', 'Tarjetas Amarillas']:
                    norm = 1 - norm
                
                puntuacion += norm * peso
        
        
        ranking = []
        for i, idx in enumerate(puntuacion.sort_values(ascending=False).index):
            jugador = datos.iloc[idx]
            ranking.append({
                'posicion': i + 1,
                'nombre': jugador['Nombre'],
                'equipo': jugador['Equipo'],
                'puntuacion': round(puntuacion[idx] * 100, 2)
            })
        
        return ranking