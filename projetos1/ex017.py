#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


'''co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = (co**2 + ca**2) **(1/2)
print('A hipotenusa desse triângulo é {:.2f}'.format(hi))'''

from math import hypot

co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa desse triângulo é {:.2f}'.format(hi))
