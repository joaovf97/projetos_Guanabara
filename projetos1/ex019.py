# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice  

a1 = input('Digite o Nome do primeiro aluno : ')
a2 = input('Digite o Nome do segundo aluno : ')
a3 = input('Digite o Nome do terceiro aluno : ')
a4 = input('Digite o Nome do quarto aluno : ')
print('O aluno sorteado para apagar o quadro é :{} '.format(choice([a1, a2, a3, a4])))


