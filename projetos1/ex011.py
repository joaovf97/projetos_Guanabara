#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


largura= int(input('Digite a largura da parede: '))
altura= int(input('Digite a altura da parade: '))
area= largura*altura
print(' A quantidade de tinta necessária para pintá-la é {} litros.'.format(area/2))