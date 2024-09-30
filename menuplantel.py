import os
import modulos.menuequipos as me

def menuplantell(planteles: dict):
    print("Este menú pertenece al plantel")
    isvalid = True
    directores_tecnicos = {}
    jugadores = {}
    Assistan_Coach = {}
    cuerpo_medico = {}
    preparador_fisico = {}
    jugador = {}
    while isvalid:
        print("1. Registrar técnico\n2. Ver Técnicos\n3. Registrar Jugador\n4. Ver Jugadores\n5. Registrar Asistente Tecnico\n6. Registrar Cuerpo medico\n7. Registrar Preparadores Fisicos\n8 Volver")
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
                    jugadores[dorsal] = {'nombre': nombre_jugador, 'dorsal': dorsal, 'posicion': posicion}
                    print(f"Jugador {nombre_jugador} registrado.")
                if opt == 2:
                    tarjetas_rojas = input(f"Ingrese tarjetas rojas para {nombre_jugador} : ")
                    tarjetas_amarillas = input(f"Ingrese tarjetas amarillas para {nombre_jugador} : ")
                    faltas_cometidas= input(f"Ingrese total faltas cometidas para {nombre_jugador} : ")
                    goles_anotados = input(f"Ingrese total goles anotados para {nombre_jugador} : ")
                    estadisticas_jugador = {f'tarjetas rojas para {nombre_jugador}': tarjetas_rojas, f'tarjetas amarillas para {nombre_jugador}': tarjetas_amarillas, f'faltas cometidas para {nombre_jugador}': faltas_cometidas, f'goles anotados para {nombre_jugador}': goles_anotados }
                    print(f"Estadisticas para {nombre_jugador} son {estadisticas_jugador} y se encuentran registradas.")
                if opt == 3:
                    print(f"Las tarjetas amarillas para {jugador} son: {tarjetas_amarillas}", f'Las tarjetas rojas son {tarjetas_rojas}')
        elif opc == 4:
            if jugadores:
                print("Los jugadores registrados son:")
                for jugador in jugadores.values():
                    print(f"Nombre: {jugador['nombre']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}")
            else:
                print("No hay jugadores registrados.")
            input("Presione cualquier tecla para continuar...")
        elif opc == 5:
            nombre_assitanCoach = input("Ingrese el nombre del asistente Tecnico: ")
            Assistan_Coach[nombre_assitanCoach] = {'nombre': nombre_assitanCoach}
            print(f"Asistente Director Tecnico {nombre_assitanCoach} registrado.")
        elif opc == 6:
            nombre_cuerpo_medico = input("Ingrese el nombre del cuerpo medico: ")
            cuerpo_medico[nombre_cuerpo_medico] = {'nombre': nombre_cuerpo_medico}
            print(f"El cuerpo medico {nombre_cuerpo_medico} registrado.")
        elif opc == 7:
            nombre_preparador_fisico = input("Ingrese el nombre del preparador fisico: ")
            preparador_fisico[nombre_preparador_fisico] = {'nombre': nombre_preparador_fisico}
            print(f"El preparador fisico {nombre_preparador_fisico} registrado.")
        elif opc == 8:
            isvalid = False
        else:
            print("Opción no válida.")


