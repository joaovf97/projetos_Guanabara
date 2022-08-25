# Exercício Python 060:
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Fatorial de: "))
resultado = 1
count = 1
while count <= numero:
    resultado *= count
    count += 1

print(resultado)
