# Exercício Python 039:
# Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
idade = int(input('Digite o ano de nascimento: '))
alistar = atual - idade
if alistar == 18:
    print('É HORA DE SE ALISTAR')
elif alistar > 18:
    print('PASSOU {} ANOS PARA SE ALISTAR'
          .format(alistar - 18))
else:
    print('AINDA FALTA {} ANOS PARA SE ALISTAR'
          .format((alistar-18) * -1))
