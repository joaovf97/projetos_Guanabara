#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
print('Média do Aluno {:.2f}'.format((n1+n2)/2))