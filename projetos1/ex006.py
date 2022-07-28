# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


n= int(input('Digite um número: '))
print('Seu dobro {} , seu triplo {} , e sua raiz quadrada {:.2f}'.format((n*2), (n*3), (n**(1/2))))