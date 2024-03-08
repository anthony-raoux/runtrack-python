def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        element_present = False
        for unique_element in liste_sans_doublons:
            if element == unique_element:
                element_present = True
                break

        if not element_present:
            liste_sans_doublons += [element]

    return liste_sans_doublons

ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
ma_liste_sans_doublons = supprimer_doublons(ma_liste)

print(ma_liste_sans_doublons)