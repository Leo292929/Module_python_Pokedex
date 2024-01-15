#import api2pokedex

from tkinter import PhotoImage
from tkinter import *
from PIL import Image, ImageTk

from Front.pokedex import affichagePokedex
from Front.combat import affichageCombat

class Launcher:
    def __init__(self, fenlauncher,pokedex):
        self.fenlauncher =fenlauncher
        self.pokedex = pokedex
        self.fenlauncher.title("Launcher")

        self.frame_bg = Frame(self.fenlauncher,height = 540, width = 960)
        self.frame_bg.pack()

        image_pillow = Image.open("Front\imageLauncher\image_background.jpg")
        self.image = ImageTk.PhotoImage(image_pillow)

        self.label_image = Label(self.frame_bg, image = self.image)
        self.label_image.place(x = 0 , y= 0)

        self.buttonLoad = Button(self.frame_bg, text = "Load" , bg = 'gray' , cursor = "arrow" , command = self.buttonLoadCommand)
        self.buttonLoad.place(x = 445, y = 235 , width = 70 , height = 25)

        self.buttonImport = Button(self.frame_bg, text = "Import" , bg = 'gray' , cursor = "arrow" , command = self.buttonImportCommand)
        self.buttonImport.place(x = 445, y = 305 , width = 70 , height = 25)
        

    def afficherMenu(self):
        self.fenlauncher.title("Menu")
        self.buttonImport.destroy
        self.buttonLoad.destroy

        self.buttonPokedex = Button(self.fenlauncher, text = "Pokedex" , bg = 'gray' , cursor = "arrow" , command = self.buttonPokedexCommand)
        self.buttonPokedex.place(x = 445, y = 235 , width = 70 , height = 25)

        self.buttonCombat = Button(self.fenlauncher, text = "Combat" , bg = 'gray' , cursor = "arrow" , command = self.buttonCombatCommand)
        self.buttonCombat.place(x = 445, y = 305 , width = 70 , height = 25)



    def buttonImportCommand(self):
        print("Import")
        self.afficherMenu()

    def buttonLoadCommand(self):
        print("load")
        self.afficherMenu()
    
    def buttonCombatCommand(self):
        self.fenlauncher.destroy()

        fencombat=Tk()
        frontpokedex = affichageCombat(fencombat,self.pokedex)
        fencombat.mainloop()
    
    def buttonPokedexCommand(self):
        self.fenlauncher.destroy()

        fenpokedex=Tk()
        frontpokedex = affichagePokedex(fenpokedex,self.pokedex)
        fenpokedex.mainloop()








