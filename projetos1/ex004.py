#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type (n))
print('Só tem espaços', n.isspace())
print('é um numero? ', n.isnumeric())
print('é alfabético? ', n.isalpha())
print('é alfanumérico', n.isalnum())
print('está em maiúsculas? ', n.isupper())
print('está em minúsculas', n.islower())
print('está capitalizada? ', n.istitle())

