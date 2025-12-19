def definir_gagnant(joueur, ordi):
    if joueur == ordi:
        return "Match Nul!"
    if (joueur == "roche" and ordi == "ciseaux") or (joueur == "ciseaux" and ordi == "papier") or (joueur == "papier" and ordi == "roche"):
        return "Vous avez gagné!"
    else:
        return "Vous avez perdu!"