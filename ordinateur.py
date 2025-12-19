import random

def choix_ordinateur():
    """
    Retourne pierre, papier ou ciseaux de façon aléatoire
    """
    return random.choice(["pierre", "papier", "ciseaux"])