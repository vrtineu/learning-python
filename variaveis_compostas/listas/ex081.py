# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()

while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    answer = ' '
    while answer not in 'yn':
        answer = str(input('Quer continuar ? [Y/N] ')).lower()
    if answer == 'n':
        break
valores.sort(reverse=True)
print(
    f'Foram digitados {len(valores)} valores, sendo eles {valores}')
if 5 in valores:
    print('O valor 5 está contido na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
