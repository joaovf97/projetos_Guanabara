# Exercício Python 028:
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint

x = randint(0, 5)
num = int(input('De 0 a 5,  em que número eu pensei? '))
if num == x:
    print('Parabens acertou o número ')
else:
    print('Errou , o numero sorteado foi {}'.format(x))
