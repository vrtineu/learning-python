# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário que ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
print('~=' * 10)
print(f'{"CADASTRO DE PESSOAS":^20}')
print('~=' * 10)

maior18 = homens = mulheres20 = 0
while True:
    age = int(input('Digite a idade: '))
    sex = str(input('Digite o sexo [M/F]: ')).lower().strip()
    if sex in 'f' or sex in 'm':
        if age >= 18:
            maior18 += 1
        if sex == 'm':
            homens += 1
        if sex == 'f' and age < 20:
            mulheres20 += 1
    else:
        print('Digite um sexo válido')
    answer = str(input('Quer continuar [Y/N]: ')).lower().strip()
    if answer == 'n':
        break
print('\nAnalisando dados...')
print(f'Foram cadastradas {maior18} pessoas maiores de 18 anos.\nForam cadastrados {homens} homens.\nForam cadastradas {mulheres20} mulheres com menos de 20 anos.')
