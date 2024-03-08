def arrondir(nombre):
    # Cette fonction arrondit un nombre à l'entier le plus proche
    partie_decimale = nombre - nombre // 1
    if partie_decimale >= 0.5:
        return nombre // 1 + 1
    else:
        return nombre // 1

def trier(liste):
    # Cette fonction trie une liste dans l'ordre croissant sans utiliser len
    n = 0
    for _ in liste:
        n += 1

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
            j += 1
        i += 1

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

ma_liste_arrondie = [arrondir(nombre) for nombre in ma_liste]

trier(ma_liste_arrondie)

print(ma_liste_arrondie)
