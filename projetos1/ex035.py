# Exercício Python 035:
# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.


a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    print('forma triângulo')
else:
    print('nao forma triângulo')
