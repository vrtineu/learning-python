# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.
# Maioridade = 21 anos.
from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input(f'Digite o {c}º ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'A quantidade de pessoas maiores de 21 anos digitadas é de {maiores}, e a quantidade de menores digitados é de {menores}.')
