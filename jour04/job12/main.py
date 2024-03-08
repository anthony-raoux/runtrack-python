def tri(liste):
    longue = len(liste)

    for i in range(longue):
        for j in range(0, longue - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri(ma_liste)

print(ma_liste)