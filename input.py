def choix_joueur():
    choix_ecrit = input("Roche, papier ou ciseaux?  ")
    if choix_ecrit == "roche" or choix_ecrit == "r":
        choix = "roche"
    elif choix_ecrit == "papier" or choix_ecrit == "p":
        choix = "papier"
    elif choix_ecrit == "ciseaux" or choix_ecrit == "ciseau" or  choix_ecrit == "c":
        choix = "ciseaux"
    else :
        choix = "erreur"
    return choix





