# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.



km= float(input('Digite a quantidade de Km percorrida: '))
dias= float(input('Digite a quantidade de dias alugados: '))
pg= (dias * 60) + (km * 0.15)
print('Total para pagamento : {:.2f} '.format(pg))
