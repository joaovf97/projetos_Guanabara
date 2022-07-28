#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo: '))
print('O seno deste ângulo é {:.2f}'.format(sin(radians(angulo))))
print('O cosseno deste ângulo é {:.2f}'.format(cos(radians(angulo))))
print('A tangente deste ângulo é {:.2f}'.format(tan(radians(angulo))))
