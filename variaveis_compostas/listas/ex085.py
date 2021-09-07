# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for valor in range(0, 7):
    num = int(input(f'Digite o {valor+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print(
    f'Os valores pares são {valores[0]}.\nOs valores ímpares são {valores[1]}.')
