import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def crear_grafico_radar(jugadores, metricas, titulo="Comparación de Jugadores"):
    """Crea un gráfico de radar para comparar jugadores"""
    num_vars = len(metricas)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Cerrar el gráfico conectando el último punto con el primero
    angles += angles[:1]
    
    # Crear la figura
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    for jugador in jugadores:
        valores = [jugador.obtener_estadisticas()[m] for m in metricas]
        valores += valores[:1]  # Cerrar el polígono
        ax.plot(angles, valores, linewidth=1, label=jugador.nombre)
        ax.fill(angles, valores, alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metricas)
    ax.set_title(titulo)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    img_path = os.path.join("static", "radar_chart.png")
    plt.savefig(img_path, bbox_inches='tight', dpi=300)
    plt.close()
    
    return img_path

def crear_grafico_barras_ranking(ranking, titulo="Ranking de Jugadores"):
    """Crea un gráfico de barras para mostrar el ranking"""
    plt.figure(figsize=(12, 6))
    nombres = [r['nombre'] for r in ranking]
    puntuaciones = [r['puntuacion'] for r in ranking]
    
    bars = plt.bar(nombres, puntuaciones)
    plt.xticks(rotation=45, ha='right')
    plt.title(titulo)
    plt.ylabel('Puntuación')
    
    # Agregar etiquetas con la posición
    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                f'#{ranking[i]["posicion"]}',
                ha='center', va='bottom')
    
    plt.tight_layout()
    
    img_path = os.path.join("static", "ranking.png")
    plt.savefig(img_path, bbox_inches='tight', dpi=300)
    plt.close()
    
    return img_path

def crear_mapa_percentiles(percentiles, jugadores, titulo="Percentiles por Estadística"):
    """Crea un mapa de calor mostrando los percentiles"""
    data = []
    nombres = [j.nombre for j in jugadores]
    metricas = list(percentiles.keys())
    
    for nombre in nombres:
        row = [percentiles[m][nombre] for m in metricas]
        data.append(row)
    
    plt.figure(figsize=(12, len(jugadores) * 0.5 + 2))
    sns.heatmap(data, annot=True, fmt='.1f', 
                xticklabels=metricas, 
                yticklabels=nombres,
                cmap='YlOrRd')
    
    plt.title(titulo)
    plt.tight_layout()
    
    img_path = os.path.join("static", "percentiles.png")
    plt.savefig(img_path, bbox_inches='tight', dpi=300)
    plt.close()
    
    return img_path