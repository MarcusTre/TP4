import math as mt

class Noeud:
    def __init__(self, valeurs, enfant=None):
        self.valeurs = valeurs #La valeur que l'on va venir prendre
        self.enfant = enfant #initialisation des attributs
        if self.enfant is None:
            self.enfant = []

    def ajouter_enfant(self,noeud):    
         if isinstance(noeud, Noeud):
            self.enfant.append(noeud.valeurs)
            #On va venir ajouter notre nouvel_enfant dans le noeud
         else:
            raise TypeError("Votre enfant doit être un noeud !!!!")
    def afficher_expression(self):

        affichage = "L'expression de notre noeud est : "
        expression = ""
        if len(self.enfant)==0 :
            affichage+="Pas d'expression dans votre noeud"

        else :
            expression = f"{self.valeurs}"
            for i in self.enfant:
                expression += f" {i}"
            affichage+=expression

        print(affichage)
    
    def evaluer(self, dico):
        if not isinstance(dico, dict):
            raise TypeError("Il me FAUT UN DICTIONNAIRE, U IDIOT !!!")
        else:
            if isinstance(self.valeurs, (float,int)):
                return self.valeurs
            if self.valeurs in dico:
                return dico[self.valeurs]
            if len(self.enfant):
                if self.valeurs == '+':
                    return self.enfant[0].evaluer(dico) + self.enfant[1].evaluer(dico)
                elif self.valeurs == '-':
                    return self.enfant[0].evaluer(dico) - self.enfant[1].evaluer(dico)
                elif self.valeurs == '*':
                    return self.enfant[0].evaluer(dico) * self.enfant[1].evaluer(dico)
            raise ValueError("opérateur/Noeud inconnu")


print("Hello Github !")