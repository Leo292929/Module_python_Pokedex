from classpokedex import equipe
from tkinter import PhotoImage
from tkinter import *
from PIL import Image, ImageTk


class affichageCombat:
    def __init__(self,fencombat,pokedex):
        self.fencombat = fencombat
        self.equipe1 = self.choix_equipe(self,pokedex,1)
        self.equipe2 = self.choix_equipe(self,pokedex,2)
        self.gagnant = self.combat(self,self.equipe1,self.equipe2)
        self.afficher_gagant(self)


    def choix_equipe(self,pokedex,j):
        i = 1
        pokemon1 = self.choix_pokemon(self,pokedex,i,j)
        i+=1
        pokemon2 = self.choix_pokemon(self,pokedex,i,j)
        i+=1
        pokemon3 = self.choix_pokemon(self,pokedex,i,)
        i+=1
        pokemon4 = self.choix_pokemon(self,pokedex,i,j)
        i+=1
        pokemon5 = self.choix_pokemon(self,pokedex,i,j)
        i+=1
        pokemon6 = self.choix_pokemon(self,pokedex,i,j)
        return equipe(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6)
    
    def choix_pokemon(self,pokedex,i,j):
        self.frame_bg = Frame(self.fencombat,height = 540, width = 960)
        self.frame_bg.pack()

        image_pillow = Image.open("Front\imageCombat\image_choix_pokemon.jpg")
        self.image = ImageTk.PhotoImage(image_pillow)

        self.label_image = Label(self.frame_bg, image = self.image)
        self.label_image.place(x = 0 , y= 0)

        

    def combat(self,equipe1):
        pass

    def afficher_gagant(self):
        print(f"le joueur {self.gagnant} a gagner!!!")

def clear_fenetre(fenetre):
    for widget in fenetre.winfo_children():
        widget.destroy()

