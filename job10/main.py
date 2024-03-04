def simulation_financiere(montant_initial, taux_rendement_annuel, nombre_annees):
    montant = montant_initial

    for annee in range(1, nombre_annees + 1):
        gain_annuel = montant * (taux_rendement_annuel / 100)
        montant += gain_annuel
        print(f"Année {annee}: Gain annuel - {gain_annuel:.2f} € | Montant total - {montant:.2f} €")

    return montant

# Paramètres initiaux
montant_initial = 10000
taux_rendement_annuel = 5

# Simulation initiale
nombre_annees = 5
resultat_final = simulation_financiere(montant_initial, taux_rendement_annuel, nombre_annees)

# Augmentation du capital et du taux de rendement
montant_initial += 5000
taux_rendement_annuel += 2

# Simulation après augmentation du capital
nombre_annees = 3
resultat_final = simulation_financiere(montant_initial, taux_rendement_annuel, nombre_annees)

# Retrait de 10% et diminution du rendement de 1%
montant_initial -= (montant_initial * 0.10)
taux_rendement_annuel -= 1

# Simulation après retrait
nombre_annees = 2
resultat_final = simulation_financiere(montant_initial, taux_rendement_annuel, nombre_annees)
