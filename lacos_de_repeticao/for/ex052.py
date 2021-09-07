# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
divisivel = 0
numero = int(input('Digite um número inteiro: '))

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end = ' ')
        divisivel += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{c}', end = ' ')
if divisivel == 2:
    print(f'\n\033[mO número {numero} é um número primo!')
else:
    print(f'\n\033[mO número {numero} NÃO é um número primo, pois foi divisível {divisivel} vezes.')
