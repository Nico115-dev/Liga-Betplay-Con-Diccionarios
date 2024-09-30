import os
def limpiarconsola():
    os.system("cls" if os.name == "nt" else "clear")