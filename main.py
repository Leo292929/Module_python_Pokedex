from api2pokedex import loadPokedemon
from api2pokedex import importPokedex
from Front.launcher import Launcher
from tkinter import *
import pickle




Reload = False

#afficheChoixImport(Reload)

try:
    pokedex = loadPokedemon()
except:
    pokedex = [""]
if len(pokedex)<152 or Reload:
    pokedex = importPokedex(Reload)
    print("imported")
else:
    print("loaded")

# afficherMenuPrincipal()


# afficherPokedex()

# AfficherMenuCombat()

fenlauncher=Tk()
launcher = Launcher(fenlauncher,pokedex)
fenlauncher.mainloop()

