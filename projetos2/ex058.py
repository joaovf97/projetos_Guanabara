# Exercício Python 058:
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

x = randint(0, 10)
num = int(input('De 0 a 10,  em que número eu pensei? '))
contador = 1
while num != x:
    num = int(input('Erroooou,  em que número eu pensei? '))
    contador += 1
print('Parabens acertou o número , foram {} tentativas para achar o número'
      .format(contador))
