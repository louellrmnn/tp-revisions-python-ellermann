#3a
def sommeNombre(a, b):
    return a + b

resultat = sommeNombre(5, 7)
print("La somme est :", resultat)


#3b
def saluer(nom):
    print(f"Bonjour, {nom} !")

saluer("Louise")


#3c
def trouverMaximum(liste):
    return max(liste)

nombres = [3, 5, 2, 8, 6]
resultat = trouverMaximum(nombres)
print("Le nombre maximum est :", resultat)