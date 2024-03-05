#Créez un programme qui affiche dans le terminal les tables de multiplications de 1 à N

#N étant un entier supérieur à zéro saisi par l’utilisateur.

#afficher le dans le terminal

n = int(input("Tapez la valeur de n "))
print("La table de multiplication de : ", n," est :")
for i in range(1,11):
    print(i , " x ", n, " = ",i*n)