def mi_funcion(dato):
    # aquí va tu código principal
    # IMPORTAMOS LIBRERIA PANDAS
    import pandas as pd 

    BASE_DATOS = pd.read_excel('data/TABLAPREMIER.xlsx', sheet_name='Hoja2')

    Nombre_Equipos = BASE_DATOS["Equipo"].unique()
    print("Los Equipos que jugaron en la PREMIER LEAGUE (2024-2025) ")
    print("En orden alfabetico son: ")
    print("-----------------------------------")
    for Orden_Equipo in sorted(Nombre_Equipos):
        print("-", Orden_Equipo)

    # Solicitaremos al USUARIO el equipo que desea ver sus JUGADORES
    def Jugadores_Equipo():
        Solicitud_Equipo = dato  # en vez de pedir input, usamos el dato recibido desde Flask
        if Solicitud_Equipo in Nombre_Equipos:
            Jugadores = BASE_DATOS[BASE_DATOS["Equipo"].str.lower() == Solicitud_Equipo.lower()]
            return Jugadores    
        else:
            print("El equipo ingresado no se encuentra en la base de datos, intentelo de nuevo :)")
            return None

    def Solicitar_Jugadores(Jugadores):
        if Jugadores is not None and len(Jugadores) > 0:
            print("-----------------------------------")
            print("Los JUGADORES del equipo son: ")
            print("- NOMBRE - - - - - POSICION - - - - - DORSAL -")
            for _, Jugador in Jugadores.iterrows():
                print("-", Jugador["Nombre"], "(", Jugador["Posicion"], ")", "#", Jugador["Dorsal"])     
        else:
            print("El equipo ingresado no se encuentra en la base de datos, revisa la ortografía e intentalo nuevamente :)")

    jugadores = Jugadores_Equipo()
    Solicitar_Jugadores(jugadores)

    # devolvemos una cadena para mostrar en la web
    return f"Se procesó el equipo '{dato}' correctamente."

# Esto evita que se ejecute automáticamente al importar
if __name__ == '__main__':
    print(mi_funcion("Arsenal"))
