# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(
            input(f'Digite um valor para adicionar ao [{line},{column}]: '))

print('-'*20)

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matriz[line][column]:^3}]', end='')
    print()
