def mi_funcion(dato):
    # aquí va tu código principal
    # IMPORTAMOS LIBRERIA PANDAS
    import pandas as pd

def obtener_equipos():
    df = pd.read_excel('data/TABLAPREMIER.xlsx', sheet_name='Hoja2')
    return sorted(df['Equipo'].unique())

def obtener_jugadores(jugador_equipo):
    df = pd.read_excel('data/TABLAPREMIER.xlsx', sheet_name='Hoja2')
    jugadores = df[df["Equipo"].str.lower() == jugador_equipo.lower()]
    if len(jugadores) > 0:
        return jugadores.to_html(classes='tabla', index=False)
    else:
        return "No se encontraron jugadores para este equipo."

    # devolvemos una cadena para mostrar en la web
    return f"Se procesó el equipo '{dato}' correctamente."

# Esto evita que se ejecute automáticamente al importar
if __name__ == '__main__':
    print(mi_funcion("Arsenal"))
