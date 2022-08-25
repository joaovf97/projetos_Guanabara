# Exercício Python 059: Crie um programa que leia dois valores e
# mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

numero1 = int(input('Digite o Primero Número: '))
numero2 = int(input('Digite o Segundo Número: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = numero1 + numero2
        print('A soma do número {} com {} é {}'
              .format(numero1, numero2, soma))
    elif opcao == 2:
        multip = numero1 * numero2
        print('A Multiplicação do número {} com {} é {}'.format(
            numero1, numero2, multip))
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('Entre {} e {} o maior valor é {}'
              .format(numero1, numero2, maior))
    elif opcao == 4:
        numero1 = int(input('Digite o Novo Primeiro Número: '))
        numero2 = int(input('Digite o Novo Segundo Número: '))
    elif opcao == 5:
        print('Programa Finalizado')
    else:
        print('Opção inválida. Tente novamente')
    print('*******' * 5)
print('Desligando')
