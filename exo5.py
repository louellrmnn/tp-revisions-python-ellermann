#5a
class Personne:
    def __init__(self, nom):
        self.nom = nom  

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom}.")  

personne1 = Personne("Louise")
personne1.se_presenter()  


#5b
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur  
        self.largeur = largeur   

    def aire(self):
        return self.longueur * self.largeur  

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)  


rectangle1 = Rectangle(5, 3)
print("Aire du rectangle :", rectangle1.aire()) 
print("Périmètre du rectangle :", rectangle1.perimetre())  


#5c
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon  

    def aire(self):
        pi = 3.14  
        return pi * (self.rayon ** 2) 

cercle1 = Cercle(4)
print("Aire du cercle :", cercle1.aire()) 
