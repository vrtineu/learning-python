# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = list()
par = list()
impar = list()

while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    answer = ' '
    while answer not in 'yn':
        answer = str(input('Quer continuar ? [Y/N] ')).lower()
    if answer == 'n':
        break
for numero in valores:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
valores.sort()
par.sort()
impar.sort()
print(
    f'Os valores listados foram: {valores}.\nOs valores pares foram: {par}.\nOs valores ímpares são: {impar}.')
