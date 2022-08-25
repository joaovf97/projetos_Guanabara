# Exercício Python 061:
# Refaça o DESAFIO 051, lendo o primeiro termo e a
# razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 1
termo = primeiro
while count <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    count += 1
print('FIM')
