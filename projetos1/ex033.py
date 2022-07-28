 #Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = int(input('Primero Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))
numeros = [n1, n2, n3]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))