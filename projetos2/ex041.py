# Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia  o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: INFANTIL
# - Até 14 anos: MIRIM
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano = int(input('ANO DA NASCIMENTO: '))
hoje = date.today().year
categ = hoje - ano
if categ <= 9:
    print('Categoria INFANTIL')
elif categ <= 14:
    print('Categoria MIRIM')
elif categ <= 19:
    print('Categoria JÚNIOR')
elif categ <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
