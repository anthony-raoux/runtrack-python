def est_lettre(caractere):
   
    return ('A' <= caractere <= 'Z') or ('a' <= caractere <= 'z')

def my_long_word(entier, chaine):
   
    mots = []  
    mot_actuel = ""

    for char in chaine:
        if est_lettre(char):
            mot_actuel += char
        elif mot_actuel:
            longueur = 0
            for _ in mot_actuel:
                longueur += 1

            if longueur > entier:
                mots += [mot_actuel]
            mot_actuel = ""

    if mot_actuel:
        longueur = 0
        for _ in mot_actuel:
            longueur += 1

        if longueur > entier:
            mots += [mot_actuel]

    return mots

seuil_longueur = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(seuil_longueur, phrase)

print(resultat)
