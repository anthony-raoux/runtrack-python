def fonc_moye(a, b, c):
    return (a + b + c) / 3

a = float(input("saisissez la première note :"))
b = float(input("saisissez la deuxième note :"))
c = float(input("saisissez la troisième note :"))

moyenne_etudiant = fonc_moye(a, b, c)

print(moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
if 11<= moyenne_etudiant <=14:
    print("Bon élève")
if 8<= moyenne_etudiant <=10:
    print("Élève moyen")
if 0<= moyenne_etudiant <=7:
    print("Élève devant faire des efforts")