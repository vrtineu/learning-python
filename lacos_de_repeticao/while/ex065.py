# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e quais foram o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = count = média = maior = menor = 0
answer = ''
while answer != 'n':
    num = int(input('Digite um número: '))
    if count == 0:
        maior = num
        menor = num
    soma += num
    count += 1
    answer = str(input('Quer continuar? [Y/N] ')).strip().lower()
    if num > maior:
        maior = num
    if num < menor:
        menor = num
média = soma / count
print(f'A média entre os números digitados é igual a {média:.2f}.')
print(f'O maior número digitado foi {maior}.')
print(f'O maior número digitado foi {menor}.')
