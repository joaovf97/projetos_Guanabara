#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome =str(input('Digite seu nome completo: '))
separado = nome.split()
print('Seu nome em UPPER é: {}'.format(nome.upper()))
print('Seu nome em LOWER é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))   
print('Seu primeiro nome é {} e ele tem {} letras'.format(separado[0],len(separado[0])))