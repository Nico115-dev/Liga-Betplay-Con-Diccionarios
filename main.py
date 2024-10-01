import modulos.menu as mn
import modulos.menuequipos as me
import modulos.menuplantel as mp
import modulos.utils as ut
planteles = {}
if (__name__ == "__main__"):
    activeMenu = True
    
    while activeMenu:
        res = mn.crearmenu()
        print(res)
        ut.limpiarconsola()
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
            activeMenu = False
