equipos = {}

def regEquipo(eq):
    print("Su equipo es:", eq)

def obtener_equipos():
    return equipos 

def pedirDatos():
    name = input("Ingrese el nombre de su equipo: ")
    datos = {
        'nombre': name,
        'jugadores': int(input("Ingrese el número de jugadores para este equipo: ")),
        'partidos_ganados': int(input("Ingrese el número de partidos ganados: ")),
        'partidos_perdidos': int(input("Ingrese el número de partidos perdidos: ")),
        'goles_a_favor': int(input("Ingrese el número de goles a favor: ")),
        'goles_en_contra': int(input("Ingrese el número de goles en contra: "))
    }
    return datos

def equipo_con_mas_goles_a_favor():
    if not equipos:
        print("No hay equipos registrados.")
        return
    max_goles = max(equipos.values(), key=lambda x: x['goles_a_favor']) # lambda se utiliza para crear funciones pequeñas y anónimas.
    print(f"El equipo con más goles a favor es: {max_goles['nombre']} con {max_goles['goles_a_favor']} goles.")

def ultimo_equipo_en_tabla():
    if not equipos:
        print("No hay equipos registrados.")
        return
    ultimo = min(equipos.values(), key=lambda x: (x['partidos_ganados'], -x['goles_a_favor']))
    print(f"El equipo en último puesto es: {ultimo['nombre']}.")

def equipo_con_mas_goles_en_contra():
    if not equipos:
        print("No hay equipos registrados.")
        return
    max_goles_contra = max(equipos.values(), key=lambda x: x['goles_en_contra'])
    print(f"El equipo con más goles en contra es: {max_goles_contra['nombre']} con {max_goles_contra['goles_en_contra']} goles.")

def submenu():
    isvalid = True
    while isvalid:
        print("\n1. Ingresar Equipo nuevo\n2. Ver equipos\n3. Equipo con más goles a favor\n4. Último equipo en la tabla\n5. Equipo con más goles en contra\n6. Salir")
        opc = int(input(":) "))
        if opc == 1:
            data = pedirDatos()
            equipos[data['nombre']] = data 
            print("Se ha registrado correctamente su equipo.")
        elif opc == 2:
            if equipos:
                print("Los equipos registrados son:")
                for nombre, datos in equipos.items():
                    print(f"{nombre}: {datos}")
            else:
                print("No hay equipos registrados.")
            input("Presione cualquier tecla para continuar...")
        elif opc == 3:
            equipo_con_mas_goles_a_favor()
            input("Presione cualquier tecla para continuar...")
        elif opc == 4:
            ultimo_equipo_en_tabla()
            input("Presione cualquier tecla para continuar...")
        elif opc == 5:
            equipo_con_mas_goles_en_contra()
            input("Presione cualquier tecla para continuar...")
        elif opc == 6:
            isvalid = False
        else:
            print("Opción no válida.")

