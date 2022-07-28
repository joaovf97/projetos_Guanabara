#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


carro = float(input('Qual era a velocidade de seu carro?  '))
if carro > 80:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    multa = (carro - 80 ) * 7 
    print('Sua multa será de R$ {:.2f}'.format(multa))