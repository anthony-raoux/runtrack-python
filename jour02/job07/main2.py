#À partir de la chaîne «abcdefghijklmnopqrstuvwxyz » * 10, 

#écrivez un programme qui récupère et affiche autant de caractères que possible de cette chaîne sous forme de suite pyramidale.


chaine = "abcdefghijklmnopqrstuvwxyz" * 10

niveau = 15  

indice_debut = 0

for i in range(1, niveau + 1):
    indice_fin = indice_debut + i * 2 - 1
    ligne = chaine[indice_debut:indice_fin].center(niveau * 2 - 1)
    print(ligne)
    indice_debut = indice_fin
