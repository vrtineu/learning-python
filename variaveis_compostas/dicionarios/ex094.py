# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

listaPessoas = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(
            input(f'Sexo de {pessoa["nome"]} [M/F]: ')).lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('Erro! Insira M ou F.')
    pessoa['idade'] = int(input(f'Idade de {pessoa["nome"]}: '))
    soma += pessoa['idade']
    listaPessoas.append(pessoa.copy())
    while True:
        answer = str(input('Quer continuar? [Y/N] ')).lower()[0]
        if answer in 'yn':
            break
        print('Erro! Insira Y ou N.')
    if answer in 'n':
        break
média = soma / len(listaPessoas)
print(
    f'A) Ao total foram cadastradas {len(listaPessoas)} pessoas.\nB) A média de idade do grupo é {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in listaPessoas:
    if p['sexo'] == 'f':
        print(f'{p["nome"]} ', end='')
print('\nD) Lista de pessoas que estão acima da média: ')
for p in listaPessoas:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('\nAplicação encerrada.')
