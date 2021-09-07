# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

firstterm = int(input('Digite o primero termo da PA desejada: '))
razão = int(input('Digite a razão da PA: '))
term = firstterm
count = 1
total = 0
more = 10
while more != 0:
    total += more
    while count <= total:
        print(f'{term} -> ', end='')
        term += razão
        count += 1
    print('Pausa')
    more = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')
