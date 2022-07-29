# Exercício Python 054:
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.

from datetime import date
menor = 0
atual = date.today().year
for i in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if atual - pessoa < 21:
        menor += 1
print('{} são Maiores e {} são menores.'.format(7 - menor, menor))
