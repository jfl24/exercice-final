import random

def choix_ordinateur():
    """
    Retourne roche, papier ou ciseaux de façon aléatoire
    """
    ordi = random.choice(["roche", "papier", "ciseaux"])
    return ordi

def choix_joueur():
    while True:
        choix_ecrit = input("Roche, papier ou ciseaux?  ").lower()     
        if choix_ecrit == "roche" or choix_ecrit == "r":
            joueur = "roche"
            return joueur
            break     
        elif choix_ecrit == "papier" or choix_ecrit == "p":
            joueur = "papier"
            return joueur
            break           
        elif choix_ecrit == "ciseaux" or choix_ecrit == "ciseau" or  choix_ecrit == "c":
            joueur = "ciseaux"
            return joueur
            break
        else:
            print("Erreur.  Veuillez recommencer.")
        
        
def definir_gagnant(joueur, ordi):
    if joueur == ordi:
        return f"Match Nul!  Le choix de l'ordinateur était aussi {ordi}."
    if (joueur == "roche" and ordi == "ciseaux") or (joueur == "ciseaux" and ordi == "papier") or (joueur == "papier" and ordi == "roche"):
        return f"Vous avez gagné!  Le choix de l'ordinateur était {ordi}."
    else:
        return f"Vous avez perdu!  Le choix de l'ordinateur était {ordi}."

def main():

    print("=== Jeu Roche / Papier / Ciseaux ===")

    ordi = choix_ordinateur()
    joueur = choix_joueur()
    resultat = definir_gagnant(joueur, ordi)

    print(resultat)

main()

