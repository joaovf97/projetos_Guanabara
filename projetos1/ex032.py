#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano desejado: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é BISSEXTO')
else:
    print('Esse ano não é BISSEXTO')