from random import randint
from colorama import Fore


def jeu():
    number = randint(1, 200)
    Chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))
    countparty = 1 # Compter les tours
    score = 0 # Initialise le score à zéro
    replay = True

    while number != Chiffre:
        if Chiffre > 200:
            print(Fore.YELLOW + 'Avertisssement : Le nombre entré est trop grand, vous devez saisir un nombre entre  1 et 200.' + Fore.RESET)
        if Chiffre < 1:
            print(Fore.YELLOW + 'Avertissement : Le nombre entré est trop petit, vous devez saisir un nombre entre 1 et 200.' + Fore.RESET)
        if Chiffre > number:
            if Chiffre - number <= 10:
                print("Tour", countparty, ": Un peu trop grand, mais vous vous rapprochez !")
            else:
                print("Tour", countparty, ": Trop grand, essayez encore.")
        else:
            if number - Chiffre <= 10:
                print("Tour", countparty, ": Un peu trop petit, mais vous vous rapprochez !")
            else:
                print("Tour", countparty, ": Trop petit, essayez encore.")

        Chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))
        countparty += 1 # Ajouter un tour


    score += 1 # Ajouter un point si la partie actuelle est gagnée
    print(Fore.GREEN + "Bravo, vous avez trouvé le nombre ! Le nombre était : ", number, "\n Vous avez trouvé le mot en ", countparty, "tours" + Fore.RESET)
    print(Fore.BLUE + "Vous possédez actuellement ", score,"points" + Fore.RESET)


    replay = input("Souhaitez-vous relancer une autre partie ? (o/n) :")
    if replay =="o" or replay == "oui" :
        replay = True
    else:
        replay = False

# Appel fonction
jeu()
