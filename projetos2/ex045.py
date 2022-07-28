# Exercício Python 045:
# Crie um programa que faça o computador jogar Jokenpô com você.

import random
print('vamos tirar no JOKENPÔ')
print('pedra')
print('papel')
print('tesoura')
jogada = str(input('Qual a sua jogada? '))
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print(computador)
print('')
if jogada == 'pedra' and computador == 'papel':
    print('papel embrulha pedra, você perdeu')

elif jogada == 'papel' and computador == 'pedra':
    print('papel embrulha pedra, você venceu')

elif jogada == 'pedra' and computador == 'tesoura':
    print('pedra quebra tesoura, você venceu')

elif jogada == 'tesoura' and computador == 'pedra':
    print('pedra quebra tesoura, você perdeu')

elif jogada == 'papel' and computador == 'tesoura':
    print('tesoura corta papel, você perdeu')

elif jogada == 'tesoura' and computador == 'papel':
    print('tesoura corta papel, você venceu')

elif jogada == computador:
    print('EMPATE')

else:
    print('jogue entre pedra, papel ou tesoura')
