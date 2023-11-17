from random import randint

"""
def jeu():
    nb=randint


number = randint(1,200)
Chiffre = int(input("Choisir un nombre entre 1 et 200:"))
while number != Chiffre:
    print('Le nombre est incorrect, essaie encore !')
    Chiffre = int(input("Choisir un nombre 1 et 200:"))
print("Bravo, tu as trouvé(e), le nombre était : ", number)
"""

def jeu():
    number = randint(1, 200)
    Chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))

    while number != Chiffre:
        print('Le nombre est incorrect, essayez encore !')
        Chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))

    print("Bravo, vous avez trouvé le nombre ! Le nombre était : ", number)


# Appel fonction
jeu()
