class Produit:
    def __init__(self, nom, prix_unitaire, quantite_en_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock

    def afficher_informations(self):
        print(f"Nom du produit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire} €")
        print(f"Quantité en stock: {self.quantite_en_stock} unités")
        print("--------------------")

    def ajouter_stock(self, quantite):
        self.quantite_en_stock += quantite
        print(f"Stock de {quantite} unités de {self.nom} ajouté avec succès.")

    def retirer_stock(self, quantite):
        if quantite <= self.quantite_en_stock:
            self.quantite_en_stock -= quantite
            print(f"{quantite} unités de {self.nom} retirées du stock avec succès.")
        else:
            print(f"Erreur : Stock insuffisant pour {self.nom}.")

    def mettre_a_jour_prix(self, pourcentage_augmentation):
        self.prix_unitaire *= (1 + pourcentage_augmentation / 100)
        print(f"Prix de {self.nom} mis à jour avec succès (augmentation de {pourcentage_augmentation}%).")

# Création des produits
produit1 = Produit("Banane", 4, 30)

# Affichage des informations des produits
produit1.afficher_informations()

# Ajout de stock
quantite_ajout_produit1 = 5

produit1.ajouter_stock(quantite_ajout_produit1)

# Affichage des informations après l'ajout de stock
produit1.afficher_informations()

# Demande à l'utilisateur de saisir la quantité à acheter
quantite_acheter_produit1 = int(input(f"Combien d'unités de {produit1.nom} souhaitez-vous acheter? "))

# Retrait du stock en fonction de l'achat
produit1.retirer_stock(quantite_acheter_produit1)

# Affichage des informations après l'achat
produit1.afficher_informations()
