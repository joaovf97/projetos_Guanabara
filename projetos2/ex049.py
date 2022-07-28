# Exercício Python 049:
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

n = int(input('digite um número: '))
for i in range(0, 11):
    print('{} X {} = {}'.format(n, i, n*i))
