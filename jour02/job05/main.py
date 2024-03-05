#Écrire un programme qui itère les nombres entiers de 1 à 100.

#Pour les multiples de trois, affichez « Fizz » au lieu du nombre

#pour les multiples de cinq, affichez « Buzz

#Pour les nombres qui sont des multiples de trois et de cinq, affichez «FizzBuzz ».

for nombre in range(101):
    if nombre % 3 == 0:
        print("Fizz")
    if nombre % 5 == 0:
        print("Buzz")
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    else:
        print(nombre)