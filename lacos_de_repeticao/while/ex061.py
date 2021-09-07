# Refaça o desafio 051, lendo o primeiro termo de uma razão PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

firstterm = int(input('Digite o primero termo da PA desejada: '))
razão = int(input('Digite a razão da PA: '))
term = firstterm
count = 1
while count <= 10:
    print(f'{term} -> ', end='')
    term += razão
    count += 1
print('Fim')
