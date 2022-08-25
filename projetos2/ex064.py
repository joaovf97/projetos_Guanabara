# Exercício Python 064:
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

total = 0
count = 0
numero = 0
numero = int(input('Digite um número [999 PARA PARAR]'))
while numero != 999:
    total += numero
    count += 1
    numero = int(input('Digite um número [999 PARA PARAR]'))
print('Foram digitados {} números e a soma deles é {}'
      .format(count, total))
# --> Eu fiz com -1 e -999 // refiz depois correto com a correção
