# Exercício Python 038: Escreva um programa que leia dois números inteiros e
# compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('Primero valor é maior ')
elif n2 > n1:
    print('Segundo valor é maior')
else:
    print('Os dois valores são iguais')
