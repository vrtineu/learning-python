# Leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    num = float(input(f'Digite o {c}º peso em kg: '))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior peso foi {maior}kg e o menor foi {menor}kg.')
