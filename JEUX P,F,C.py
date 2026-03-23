import random
choix= ["pierre","feuille","ciseaux"]
score_joueur = 0
score_ordi=0
while True:
    joueur= input("Pierre, feuille, ciseaux ? ").lower()
    ordi= random.choice(choix)
    print("Vous avez choisi: " , joueur)
    print("L'ordi a choisi: " , ordi)
    if joueur not in choix:
        print("choix invalide")
    elif joueur == ordi:
        print("Egalite")
        print(f'score joeur:' , {score_joueur} , 'Score ordi:' ,{score_ordi})
    elif ((joueur == "ciseaux") and (ordi == "feuille")) or ((joueur == "pierre") and (ordi == "ciseaux")) or ((joueur == "feuille") and (ordi == "pierre")):
        score_joueur = score_joueur + 1
        print("vous avez gagné")
        print(f'score joeur:' , {score_joueur} , 'Score ordi:' ,{score_ordi})
    else:
        score_ordi = score_ordi + 1
        print("vous avez perdu")
        print(f'score joueur:' , {score_joueur} , 'Score ordi:' ,{score_ordi})
    reponse= input("Tu veux rejouer ? (oui/non) : ")
    if reponse == "non":
        break
