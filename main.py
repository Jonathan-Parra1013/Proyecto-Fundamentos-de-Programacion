import pandas as pd

def mi_funcion(dato):
    # Cargar los datos
    BASE_DATOS = pd.read_excel('data/TABLAPREMIER.xlsx', sheet_name='Hoja2')

    # Obtener lista de equipos
    Nombre_Equipos = BASE_DATOS["Equipo"].unique()

    # Buscar jugadores del equipo ingresado
    equipo_filtrado = BASE_DATOS[BASE_DATOS["Equipo"].str.lower() == dato.lower()]

    # Si no encuentra el equipo
    if equipo_filtrado.empty:
        return f"El equipo '{dato}' no se encuentra en la base de datos. Intenta con uno de estos: {', '.join(sorted(Nombre_Equipos))}"

    # Construir la respuesta
    resultado = f"<h3>Jugadores del equipo {dato}:</h3><ul>"
    for _, jugador in equipo_filtrado.iterrows():
        resultado += f"<li>{jugador['Nombre']} — {jugador['Posicion']} (#{jugador['Dorsal']})</li>"
    resultado += "</ul>"

    return resultado

# Esto evita que se ejecute automáticamente al importar
if __name__ == '__main__':
    print(mi_funcion("Arsenal"))
