#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da viagem: '))
if distancia <= 200 :
    preco1 = distancia * 0.50 
    print('O valor total de sua viagem é R${:.2F}'.format(preco1))
else :
    preco2 = distancia * 0.45 
    print('O valor total de sua viagem é R${:.2F}'.format(preco2))