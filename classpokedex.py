class pokemonespece:
    def __init__(self,nom,id,description,sprite,listemoves,basestat,capspe,type1,type2 = None ):
        self.nom = nom
        self.id = id
        self.description = description
        self.sprite = sprite
        self.listemoves = listemoves
        self.basestat = basestat
        self.capspe = capspe
        self.type1 = type1
        self.type2 = type2
        print(f"le pokemon n°{self.id}: {self.nom} a bien été importé")

    def getSprite(self):
        return f"spriteFolder\{self.id}.png"

class pokemon(pokemonespece):
    def __init__(self,nom,id,description,sprite,listemoves,basestat,capspe,lvl,type1,type2 = None, moove1  = None , moove2 = None, moove3 = None, moove4 = None):
        super().__init__(self,nom,id,description,sprite,listemoves,basestat,capspe,type1,type2 = None )
        self.vivant = True
        self.lvl = lvl
        self.stat = [x * lvl for x in basestat]
        self.type1 = type1
        self.type2 = type2
        self.moove1 = moove1
        self.moove2 = moove2
        self.moove3 = moove3
        self.moove4 = moove4
        print (f"Vous avez ajouté le pokemon {self.nom} à votre equipe;\nVous lui avez appris les mooves:\n")
        if moove1!=None:
            print(moove1)
        else:
            print("Trempette")
        if moove2!=None:
            print(moove2)
        if moove3!=None:
            print(moove3)
        if moove4!=None:
            print(moove4)
    
    def attaque(self,moove,pokemonAdverse):
        pass
    
    def checkVivant(self):
        if self.stat[0] <1:
            print("ce pokemon n'as plus de pv")
            self.vivant = False

class equipe():
    def __init__(self,pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,combattant):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5
        self.pokemon6 = pokemon6
        self.combatant = self.pokemon1
    
    def checkloose(self):
        if self.pokemon1.vivant == False and self.pokemon2.vivant == False and self.pokemon3.vivant == False and self.pokemon4.vivant == False and self.pokemon5.vivant == False and self.pokemon6.vivant == False:
            print("tout vos pokemon sont hors de combat, vous avez perdu")
    def change_combattant(self):
        pass
    
