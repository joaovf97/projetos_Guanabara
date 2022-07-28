# Exercício Python 048:
# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
c = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        s = s + i
        c = c + 1
print('A soma de todos os {} valores são {}'.format(c, s))
