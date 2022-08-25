# Exercício Python 030: Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
cal = num % 2
if cal == 0:
    print('O número {} é PAR '.format(num))
else:
    print('O número {} é IMPAR'.format(num))
