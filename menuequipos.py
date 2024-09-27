import os
equipos = []
def regEquipo(eq:list):
    equipo = eq
    print("Su equipo es: ", equipo)
def obtener_equipos():
    return equipos 
def pedirDatos():
    name = str(input("Ingrese el nombre de su equipo: "))
    datos = [name, 0, 0, 0, 0, 0, 0]
    return datos
def submenu():
    isvalid = True
    while isvalid:
        print("1. Ingresar Equipo nuevo\n2. Ver equipos\n3. Salir\n")
        opc = int(input(": "))
        if opc == 1:
            data = pedirDatos()
            equipos.append(data)
            print("Se ha registrado correctamente su equipo.")
        elif opc == 2:
            if equipos:
                print("Los equipos registrados son:")
                for eq in equipos:
                    print(eq)
            else:
                print("No hay equipos registrados.")
            input("Presione cualquier tecla para continuar...")
        elif opc == 3:
            isvalid = False
        else:
            print("Opción no válida.")