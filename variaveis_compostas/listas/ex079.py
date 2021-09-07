# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor válido, adicionado à lista.')
    else:
        print('Valor já adicionado à lista, não será adicionado a lista.')

    answer = str(input('Quer continuar? [Y/N] ')).lower()
    if answer in 'n':
        break
valores.sort(reverse=False)
print(f'A lista de números digitados foi {valores}.')
