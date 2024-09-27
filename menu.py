import os 

def crearmenu():
    options ={
                1: "Registro equipos torneo",
                2: "Registro plantel",
                3: "Programar partidos",
                4: "Registrar resultado fecha",
                5: "Salir"
            }
    valid = True
    while valid:
        try:
            print("*****************************************************")
            print("****               LIGA BETPLAY                  ****")
            print("*****************************************************")

            for key,valor in options.items():
                 print(f"{key}. {valor}")
            result = int(input("Ingrese un numero para ir a ese menu: "))
            if not (result in options):
                print("Su opción no es valida, escoja otra: ")
                os.system("pause")
                os.system("cls")
                return crearmenu()
        except ValueError as a:
            print(f"El dato no es valido {a}")

            os.system("pause")
            os.system("cls")
            crearmenu()
        else:
            valid = False
            return result
