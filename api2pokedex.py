# -*- coding: utf-8 -*-

import requests
import classpokedex
import time
import os
import pickle


def importPokedex(Reload = False,n=151):


    
    temps_debut = time.time()
    


    napi = "https://pokeapi.co/api/v2/"
    pokedex = [""]

    if not os.path.exists("pokedexFolder"):
        print(" pokedexFolder")
        os.makedirs("pokedexFolder")


    for i in range(n):

        id = i+1
        if Reload or (not os.path.exists(f"pokedexFolder\{id}.pkl")):
            dataspecies = (requests.get(f'{napi}pokemon-species/{id}')).json()
            datapokemon = (requests.get(f'{napi}pokemon/{id}')).json()
            nom = dataspecies["name"]
            description = dataspecies["genera"][3]["genus"]
            sprite = (f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{str(i+1)}.png")
            listemoves = []
            for e in datapokemon["moves"]:
                listemoves.append(e["move"]["name"])
            basestat = []
            for e in datapokemon["stats"]:
                basestat.append(e["base_stat"])
            capspe = []
            for e in datapokemon["abilities"]:
                capspe.append(e["ability"]["name"])
            type1 = datapokemon["types"][0]["type"]["name"]
            if len(datapokemon["types"])>1:
                type2 = datapokemon["types"][1]["type"]["name"]
                pokemon = classpokedex.pokemonespece(nom,id,description,sprite,listemoves,basestat,capspe,type1,type2)
            else:
                pokemon = classpokedex.pokemonespece(nom,id,description,sprite,listemoves,basestat,capspe,type1)
            pokedex.append(pokemon)

            with open(f"pokedexFolder\{id}.pkl", "wb") as fichier:
                pickle.dump(pokemon, fichier)
            





    temps_fin = time.time()
    if n == 151:
        temps_ecoule = temps_fin - temps_debut
        print(f"Le programme a mis {temps_ecoule} secondes à s'exécuter.")
        nom_fichier = "temps_execution.txt"
        with open(nom_fichier, "a") as fichier:
            fichier.write(str(temps_ecoule))
            fichier.write("\n")


    if not os.path.exists("spriteFolder"):
        print(" creation de spriteFolder")
        os.makedirs("spriteFolder")

    for e in pokedex[1:]:
        if not os.path.exists(f"spriteFolder\{e.id}.png"):
            url = e.sprite
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"spriteFolder\{e.id}.png", "wb") as file:
                    file.write(response.content)
                print(f"Image {e.id} téléchargée avec succès.")
            else:
                print(f"Échec du téléchargement. Code d'état HTTP : {response.status_code}")


    

    return pokedex



def loadPokedemon():
    pokedex = [""]
    folder = "pokedexFolder"
    listFiles = sorted(os.listdir(folder), key=lambda x: int(x.split('.')[0]))
    PathlistFiles = [os.path.join(folder, fichier) for fichier in listFiles]
    for e in PathlistFiles:
        with open(e, "rb") as fichier:
            pokemon = pickle.load(fichier)
            pokedex.append(pokemon)
    return pokedex




# pokedexdata = "pokedexdata.py"
# with open(pokedexdata, "a") as fichier:
#      fichier.write(str())
#      fichier.write("\n")

