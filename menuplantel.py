import os
import modulos.menuequipos as me

def menuplantell(planteles: dict):
    print("Este menú pertenece al plantel")
    isvalid = True
    directores_tecnicos = {}
    jugadores = {}
    Asistente_Coach = {}
    cuerpo_medico = {}
    preparador_fisico = {}
    contador = 1
    
    while isvalid:
        print("1. Registrar técnico\n2. Ver Técnicos\n3. Registrar Jugador\n4. Ver Jugadores\n5. Registrar Asistente Técnico\n6. Registrar Cuerpo Médico\n7. Registrar Preparadores Físicos\n8. Volver")
        opc = int(input(": "))
        
        if opc == 1:
            nombre_dt = input("Ingrese el nombre del director técnico: ")
            directores_tecnicos[nombre_dt] = {'nombre': nombre_dt}
            print(f"Director técnico {nombre_dt} registrado.")
        
        elif opc == 2:
            if directores_tecnicos:
                print("Los directores técnicos registrados son:")
                for dt in directores_tecnicos.values():
                    print(f"Nombre: {dt['nombre']}")
            else:
                print("No hay directores técnicos registrados.")
            input("Presione cualquier tecla para continuar...")
        
        elif opc == 3:
            print("1. Ingresar un jugador\n2. Ingresar Tarjetas para jugador\n3. Ver Tarjetas")
            opt = int(input(": "))
            
            if opt == 1:
                nombre_jugador = input("Ingrese el nombre del jugador: ")
                dorsal = input("Ingrese el dorsal del jugador: ")
                posicion = input("Ingrese la posición del jugador: ")
                jugador = {
                    "nombre": nombre_jugador,
                    "dorsal": dorsal,
                    "Posición": posicion,
                    "estadisticas": {}
                }
                print("Se ha registrado su jugador correctamente")
                jugadores[str(contador).zfill(2)] = jugador
                contador += 1
            
            elif opt == 2:
                print("Escoja un jugador a registrar las estadísticas: ")
                for id_jugador, jugador in jugadores.items():
                    print(f"id: {id_jugador}, Nombre: {jugador['nombre']}")
                id_jugador = input("Ingrese el ID del jugador: ").zfill(2)
                
                if id_jugador in jugadores:
                    tarjetas_rojas = input(f"Ingrese tarjetas rojas para {jugadores[id_jugador]['nombre']}: ")
                    tarjetas_amarillas = input(f"Ingrese tarjetas amarillas para {jugadores[id_jugador]['nombre']}: ")
                    faltas_cometidas = input(f"Ingrese total faltas cometidas para {jugadores[id_jugador]['nombre']}: ")
                    goles_anotados = input(f"Ingrese total goles anotados para {jugadores[id_jugador]['nombre']}: ")
                    
                    jugadores[id_jugador]["estadisticas"] = {
                        "tarjetas_rojas": tarjetas_rojas,
                        "tarjetas_amarillas": tarjetas_amarillas,
                        "faltas_cometidas": faltas_cometidas,
                        "goles_anotados": goles_anotados
                    }
                    print(f"Estadísticas para {jugadores[id_jugador]['nombre']} registradas.")
                else:
                    print("Jugador no encontrado.")
            
            elif opt == 3:
                print("Escoja un jugador para ver las tarjetas: ")
                for id_jugador, jugador in jugadores.items():
                    print(f"id: {id_jugador}, Nombre: {jugador['nombre']}")
                id_jugador = input("Ingrese el ID del jugador: ").zfill(2)
                
                if id_jugador in jugadores:
                    estadisticas = jugadores[id_jugador]["estadisticas"]
                    print(f"Las tarjetas amarillas para {jugadores[id_jugador]['nombre']} son: {estadisticas.get('tarjetas_amarillas', 'No registradas')}, "
                          f"Las tarjetas rojas son: {estadisticas.get('tarjetas_rojas', 'No registradas')}, "
                          f"Los goles son: {estadisticas.get('goles_anotados', 'No tiene goles')}")
                else:
                    print("Jugador no encontrado.")
        
        elif opc == 4:
            if jugadores:
                print("Los jugadores registrados son:")
                for id_jugador, jugador in jugadores.items():
                    print(f"id: {id_jugador}, Nombre: {jugador['nombre']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['Posición']}")
            else:
                print("No hay jugadores registrados.")
            input("Presione cualquier tecla para continuar...")
        
        elif opc == 5:
            nombre_asistente_coach = input("Ingrese el nombre del asistente técnico: ")
            Asistente_Coach[nombre_asistente_coach] = {'nombre': nombre_asistente_coach}
            print(f"Asistente técnico {nombre_asistente_coach} registrado.")
        
        elif opc == 6:
            nombre_cuerpo_medico = input("Ingrese el nombre del cuerpo médico: ")
            cuerpo_medico[nombre_cuerpo_medico] = {'nombre': nombre_cuerpo_medico}
            print(f"El cuerpo médico {nombre_cuerpo_medico} registrado.")
        
        elif opc == 7:
            nombre_preparador_fisico = input("Ingrese el nombre del preparador físico: ")
            preparador_fisico[nombre_preparador_fisico] = {'nombre': nombre_preparador_fisico}
            print(f"El preparador físico {nombre_preparador_fisico} registrado.")
        
        elif opc == 8:
            isvalid = False
        
        else:
            print("Opción no válida.")

