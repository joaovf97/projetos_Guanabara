# Exercício Python 037:
# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.


numero = int(input('Digite um número: '))
print('Opções para conversão : ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Digite a opção desejada para a conversão: '))
if opcao == 1:
    print('O número {} convertido para Binário é {}'
          .format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para Octal é {}'
          .format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é {}'
          .format(numero, hex(numero)[2:]))
