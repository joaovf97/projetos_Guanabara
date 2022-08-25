# Exercício Python 063:
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

termos = int(input('Digite quantos termos você quer mostrar? '))
numero = 1
termo1 = 0
termo2 = 1
while numero <= termos:
    print('{}'.format(termo1), end='')
    total = termo1 + termo2
    termo1 = termo2
    termo2 = total
    print(" -> " if numero < termos else " >> FIM", end="")
    numero += 1
