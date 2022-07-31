# Exercício Python 056:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


# NÃO CONSEGUI FAZER SOZINHO

somaIdade = 0
mediaIdade = 0
maioridadeHomem = 0
nomeVelho = ''
totalMulher = 0
for i in range(1, 5):
    nome = str(input('Digite o NOME da {}ª pessoa: '.format(i)))
    idade = int(input('Digite o IDADE da pessoa: '))
    sexo = str(input('Digite o SEXO da pessoa (M/F): '))
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'
      .format(maioridadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalMulher))
