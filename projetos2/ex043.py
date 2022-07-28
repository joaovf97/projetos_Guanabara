# Exercício Python 043:
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc >= 40.0:
    print('Obesidade mórbida')
elif imc >= 30.0 <= 40.0:
    print('Obesidade')
elif imc >= 25.0 <= 30.0:
    print('Sobrepeso')
elif imc >= 18.0 <= 25.0:
    print('Peso ideal')
else:
    print('Abaixo do peso normal')
