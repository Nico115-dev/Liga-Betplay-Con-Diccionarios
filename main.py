import modulos.menu as mn
import modulos.menuEquipos as me
import modulos.menuplantel as mp
import modulos.programarPartidos as pp
import modulos.resultadoFecha as rf

if (__name__ == "__main__"):

    equipos = []
    planteles = []
    partidos_programados = []
    resultados = []
    activeMenu = True
    
    while activeMenu:
        res = mn.crearMenu()
        print(res)
        if res == 1:
            try:
                me.submenu()
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")
        elif res == 2:
            try:
                mp.menuplantell(planteles)
            except ValueError:
                print("Ha ocurrido un error")
        elif res == 3:
            try:
                pp.encuentros(partidos_programados)  
            except Exception as e:
                print(f"Error al programar partidos: {e}")
        elif res == 4:
            try:
                if partidos_programados:
                    for partido in partidos_programados:
                        resultado = rf.registrar_resultado(partido)
                        resultados.append(resultado)  
                else:
                    print("No hay partidos programados.")
            except Exception as e:
                print(f"Error al registrar resultados: {e}")
        elif res == 5:
            activeMenu = False
