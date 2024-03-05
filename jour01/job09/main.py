# création des variables : nom, prix_unitaire, quandtité_en_stock, inflation,

#j'affiche le contenu des 3 variables de façon formatté (utiliser les f string)

#demander à l'utilisateur de saisir la quantité de produits qu'il souhaite acheter (voir methode input())

#je mets ma variable quantité_stock à jour : quandtité_en_stock - ce que l'utilisateur a acheter

#j'affiche  de nouveau le contenu des 3 variables de façon formatté (utiliser les f string) mais avec le pris qui a suivi l'inflation

# demander = input, si = if, afficher = print


nom = "banane"

prix_unitaire = "4€"

quantite_en_stock = "20"

inflation = "10%"

print(f'informations du produit {nom=} {prix_unitaire=} {quantite_en_stock=}')

acheter_nom = int(input(f"Combien d'unités de {nom} souhaitez-vous acheter? "))

