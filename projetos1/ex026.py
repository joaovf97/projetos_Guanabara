#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

n1 = str(input('Digite uma frase : ')).strip().lower()
print('A primeira letra A aparece na posiçao {}'.format(n1.find('a')+1))
print('A Ultima letra A aparece na posiçao {}'.format(n1.rfind('a')+1))
print('A  letra A aparece {} vezes na frase'.format(n1.count('a')))