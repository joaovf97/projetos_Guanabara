# Exercício Python 044:
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Qual é o Valor do Produto? R$ '))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à Vista Dinheiro / Cheque
[ 2 ] à Vista no Cartão de Crédito
[ 3 ] 2x no Cartão de Crédito
[ 4 ] 3x ou mais no Cartão de Crédito
Qual é a Opção? '''))

aVista = produto / 100 * 90
creditoAvista = produto / 100 * 95
juros = produto / 100 * 120

if pagamento == 1:
    print(
        'O Valor do Produto Ficará R$ {:.2f} à Vista no Dinheiro / Cheque.'
        .format(aVista))
elif pagamento == 2:
    print('O Valor do Produto Ficará R$ {:.2f} à Vista no Cartão de Crédito.'
          .format(creditoAvista))
elif pagamento == 3:
    print('Sua Compra será Parcelada em 2x de R$ {:.2f}\n'
          'Sua Compra vai Custar R$ {:.2f}.'.format(produto/2, produto))
elif pagamento == 4:
    parcelas = int(input('Quantas Parcelas? '))
    if parcelas >= 3:
        print('Sua Compra será Parcelada em {}x de R$ {:.2f} COM JUROS\n'
              'Sua Compra de R$ {:.2f}, Vai Custar R$ {:.2f}.'
              .format(parcelas, juros / parcelas, produto, juros))
    elif parcelas == 1:
        print(
            'O Valor do Produto Ficará R$ {:.2f} à Vista no Dinheiro / Cheque.'
            .format(aVista))
    elif parcelas == 2:
        print(
            'O Valor do Produto Ficará R$ {:.2f} à Vista no Cartão.'
            .format(creditoAvista))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO.')
