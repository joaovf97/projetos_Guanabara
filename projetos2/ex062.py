# Exercício Python 062:
# Melhore o DESAFIO 061,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:      # <--- TREINAR MAIS
    total += mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        count += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM')
