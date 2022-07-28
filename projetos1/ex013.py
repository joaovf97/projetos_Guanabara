#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario= float(input('Digite o salário do funcionário: '))
aumento=  salario* 0.15
novoSalario = salario+aumento
print('O novo salário do funcionário é {}'.format(novoSalario))