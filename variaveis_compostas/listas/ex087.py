# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

sumpar = max = sum3column = 0

for line in range(0, 3):
    for column in range(0, 3):
        matriz[line][column] = int(
            input(f'Digite um valor para adicionar ao [{line},{column}]: '))

print('-'*15)

for line in range(0, 3):
    sum3column += matriz[line][2]
    for column in range(0, 3):
        print(f'[{matriz[line][column]:^3}]', end='')
        if matriz[line][column] % 2 == 0:
            sumpar += matriz[line][column]

        if column == 0 or matriz[1][column] > max:
            max = matriz[1][column]
    print()
print('-'*15)
print(
    f'A soma dos valores pares é igual a {sumpar}.\nA soma dos valores da terceira coluna é igual a {sum3column}.\nO maior valor da segunda linha é igual a {max}.')
