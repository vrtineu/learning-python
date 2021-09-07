# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
print('~=' * 10)
print(f'{"LOJA SÃO JOSE":-^20}')
print('~=' * 10)

total = mais1000 = menorValor = count = 0
maisBarato = ''
while True:
    nomeProduto = str(input('Nome do produto: ')).strip()
    preço = int(input('Preço do produto R$'))
    if count == 0 or preço < menorValor:
        menorValor = preço
        maisBarato = nomeProduto
    total += preço
    if preço >= 1000:
        mais1000 += 1
    answer = ' '
    while answer not in 'yn':
        answer = str(input('Quer continuar [Y/N]: ')).lower()[0]
    if answer == 'n':
        break
    count += 1
print('~=' * 10)
print(
    f'Analisando...\nO total da compra é de R${total:.2f}.\nNesse total, {mais1000} produto(s) tem preço maior que R$1000,00.\nO produto mais barato foi {maisBarato}.')
