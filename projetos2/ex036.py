# Exercício Python 036: Escreva um programa para aprovar
# o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e
#  em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
#  então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
ano = float(input('Digite quantos anos de financiamento: '))
prestacao = casa / (ano * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos , a prestação será de {:.2f}'
      .format(casa, ano, prestacao))
if prestacao >= minimo:
    print('EMPRESTIMO REPROVADO')
else:
    print('EMPRESTIMO APROVADO')
