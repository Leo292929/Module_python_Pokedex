from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
class affichagePokedex:
    def __init__(self, fenpokedex,pokedex=[]):
        self.pokedex = pokedex
        self.fenpokedex = fenpokedex
        self.fenpokedex.title("pokedex")

        self.frame_bg = Frame(self.fenpokedex,height = 541, width = 745)
        self.frame_bg.pack()

        image_pillow = Image.open("Front\imagepokedex\pokedex1.png")
        self.image = ImageTk.PhotoImage(image_pillow)

        self.label_image = Label(self.frame_bg, image = self.image)
        self.label_image.place(x = 0 , y= 0)

        self.canvas_image = Canvas(self.frame_bg,bg = "green3",height = 170, width = 257,borderwidth=4)
        self.canvas_image.place(x = 47 , y = 150)
        
        self.canvas_description = Canvas(self.frame_bg,bg = "green3",height = 104, width = 234,borderwidth=4)
        self.canvas_description.place(x = 448 , y = 163)

        self.scrollbar_y = Scrollbar(self.frame_bg, orient="vertical", command=self.canvas_image.yview)
        self.scrollbar_y.place(x = 313 , y = 150,height=182)
        self.canvas_image.config(yscrollcommand=self.scrollbar_y.set)
        self.fenpokedex.bind("<MouseWheel>", self.on_scroll)
        self.fenpokedex.grid_rowconfigure(0, weight=1)
        self.fenpokedex.grid_columnconfigure(0, weight=1)
        self.canvas_image.config(scrollregion=(0, 0, 100, 10+85*(len(pokedex[1:])//3+1)))

        
        self.liste_sprite,i,j = [],2,-1
        for e in pokedex[1:]:
            
            image_pokemon_pillow_image = Image.open(e.getSprite())
            self.image_pokemon = ImageTk.PhotoImage(image_pokemon_pillow_image)
            self.liste_sprite.append(self.image_pokemon)
            
            if i == 2 : 
                i = 0
                j+=1
            else : 
                i+=1

            x = 85*i-3
            y = 5 + 85*j

            self.canvas_image.create_image(x,y,anchor=NW, image=self.liste_sprite[-1])

        self.canvas_image.bind('<Button-1>', self.clique_souris_canvas)


        self.selection_combobox = StringVar()
        self.liste_nom_pokemon = []
        for e in pokedex[1:]:
            self.liste_nom_pokemon.append(e.nom)
        self.liste_deroulante = ttk.Combobox(self.frame_bg, textvariable=self.selection_combobox,values = self.liste_nom_pokemon)
        self.liste_deroulante.place(x = 169, y = 345)
        self.label_image.bind('<Button-1>', self.clique_souris_bouton_rouge)

        image_pokemon_pillow_description = Image.open(pokedex[1].getSprite())
        self.image_pokemon_description = ImageTk.PhotoImage(image_pokemon_pillow_description)
        self.image_description_id = self.canvas_description.create_image(5,10,anchor=NW, image=self.image_pokemon_description)
        self.plan_description = self.canvas_description.create_text(95,10,anchor=NW,text = f"Name :                        N°\n\nType(s):")
        self.nom_description = self.canvas_description.create_text(135,10,anchor=NW,text = f"{self.pokedex[1].nom}")
        self.id_description = self.canvas_description.create_text(222,10,anchor=NW,text = f"{pokedex[1].id}")
        self.type1_description = self.canvas_description.create_text(140,40,anchor=NW,text = f"{pokedex[1].type1}")
        self.description_texte = self.canvas_description.create_text(95,65,anchor=NW,text = f"{pokedex[1].description} ")

    def on_scroll(self,event):
        self.canvas_image.yview_scroll(-1 * int(event.delta / 120), "units")


    
    def afficher_pokemon(self, pokemon):



        self.canvas_description.delete(self.image_description_id)
        self.canvas_description.delete(self.nom_description)
        self.canvas_description.delete(self.id_description)
        self.canvas_description.delete(self.type1_description)
        self.canvas_description.delete(self.description_texte)
        

        image_pokemon_pillow_description = Image.open(pokemon.getSprite())
        self.image_pokemon_description = ImageTk.PhotoImage(image_pokemon_pillow_description)
        self.canvas_description.create_image(5,10,anchor=NW, image=self.image_pokemon_description) 

        self.nom_description = self.canvas_description.create_text(135,10,anchor=NW,text = f"{pokemon.nom}")
        self.id_description = self.canvas_description.create_text(222,10,anchor=NW,text = f"{pokemon.id}")

        
        if pokemon.type2 != None:
            self.type1_description = self.canvas_description.create_text(140,40,anchor=NW,text = f"{pokemon.type1} / {pokemon.type2}")
        else:
            self.type1_description = self.canvas_description.create_text(140,40,anchor=NW,text = f"{pokemon.type1}")


        self.description_texte = self.canvas_description.create_text(95,65,anchor=NW,text = f"{pokemon.description} ")

    def clique_souris_canvas(self, event):

        x = event.x
        y = int(self.canvas_image.canvasy(event.y))

        i = x//85+1
        j = y//85
        id = 3*j + i

        self.afficher_pokemon(self.pokedex[id])
    
    def clique_souris_bouton_rouge(self, event):

        x = event.x
        y = event.y

        if x>90 and x<120 and y>340 and y <380:

            nom_pokemon = self.selection_combobox.get()
            for e in self.pokedex[1:]:
                if e.nom == nom_pokemon:
                    self.afficher_pokemon(e)

        #self.afficher_pokemon(self.pokedex[id])


