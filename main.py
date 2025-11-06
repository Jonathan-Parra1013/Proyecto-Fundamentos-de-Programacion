def mi_funcion(dato):
    import pandas as pd 

    BASE_DATOS = pd.read_excel('data/TABLAPREMIER.xlsx', sheet_name='Hoja2')

    Nombre_Equipos = BASE_DATOS["Equipo"].unique()
    salida = ""  # aquí guardaremos todo el texto para mostrarlo también en la web

    salida += "Los Equipos que jugaron en la PREMIER LEAGUE (2024-2025)\n"
    salida += "En orden alfabético son:\n"
    salida += "-----------------------------------\n"
    for Orden_Equipo in sorted(Nombre_Equipos):
        salida += f"- {Orden_Equipo}\n"

    print(salida)

    # Solicitaremos al USUARIO el equipo que desea ver sus JUGADORES
    def Jugadores_Equipo():
        Solicitud_Equipo = dato  # lo que viene desde Flask
        if Solicitud_Equipo in Nombre_Equipos:
            Jugadores = BASE_DATOS[BASE_DATOS["Equipo"].str.lower() == Solicitud_Equipo.lower()]
            return Jugadores    
        else:
            mensaje = "El equipo ingresado no se encuentra en la base de datos, inténtelo de nuevo :)\n"
            print(mensaje)
            return None

    def Solicitar_Jugadores(Jugadores):
        texto = ""
        if Jugadores is not None and len(Jugadores) > 0:
            texto += "-----------------------------------\n"
            texto += "Los JUGADORES del equipo son:\n"
            texto += "- NOMBRE - - - - - POSICION - - - - - DORSAL -\n"
            for _, Jugador in Jugadores.iterrows():
                linea = f"- {Jugador['Nombre']} ({Jugador['Posicion']}) #{Jugador['Dorsal']}\n"
                texto += linea
            print(texto)
        else:
            texto = "El equipo ingresado no se encuentra en la base de datos, revisa la ortografía e inténtalo nuevamente :)\n"
            print(texto)
        return texto

    jugadores = Jugadores_Equipo()
    texto_jugadores = Solicitar_Jugadores(jugadores)

    # devolvemos todo el texto para mostrar en la web
    return f"<pre>{salida}\n{texto_jugadores}</pre>"

# Esto evita que se ejecute automáticamente al importar
if __name__ == '__main__':
    print(mi_funcion("Arsenal"))
