# /!\ Il faut installer colorama et pytictoc avec pip avant de pouvoir executer le programme
from random import *
from colorama import *
from pytictoc import *

t = TicToc()


def jeu(countparty=1, countgame=1, score=0):
    number = randint(1, 200)
    chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))
    t.tic()

    while number != chiffre:
        if chiffre > 200:
            print(
                Fore.YELLOW + 'Avertissement : Le nombre entré est trop grand, vous devez saisir un nombre entre 1 et 200.' + Fore.RESET)
        if chiffre < 1:
            print(
                Fore.YELLOW + 'Avertissement : Le nombre entré est trop petit, vous devez saisir un nombre entre 1 et 200.' + Fore.RESET)
        if chiffre > number:
            if chiffre - number <= 10:
                print("Tour", countparty, ": Un peu trop grand, mais vous vous rapprochez !")
            else:
                print("Tour", countparty, ": Trop grand, essayez encore.")
        else:
            if number - chiffre <= 10:
                print("Tour", countparty, ": Un peu trop petit, mais vous vous rapprochez !")
            else:
                print("Tour", countparty, ": Trop petit, essayez encore.")

        chiffre = int(input("Choisissez un nombre entre 1 et 200 : "))
        countparty += 1

    
    score += 2
    print(Fore.GREEN + "Bravo, vous avez trouvé le nombre ! Le nombre était : ", number,
          "\n Vous avez trouvé le mot en ", countparty, "tours" + Fore.RESET)
    print(Fore.BLUE + "Vous possédez actuellement ", score, "points" + Fore.RESET)
    print(Fore.MAGENTA + "Vous avez effectué(e) ", countgame, "parties" + Fore.RESET)
    t.toc()

    replay = input("Souhaitez-vous relancer une autre partie ? (o/n) :")
    if replay == "o" or replay == "oui":
        countgame += 1
        jeu(countparty=1, countgame=countgame, score=score)  # Réinitialiser countparty pour la nouvelle partie
    else:
        print(Fore.RED + "Fin." + Fore.RESET)
        pass

# Appel fonction
jeu()