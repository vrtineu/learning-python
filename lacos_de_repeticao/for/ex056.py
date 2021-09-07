# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1, 5):
    print(f'---- {i}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: ')).strip().lower()
    somaidade += idade
    if idade > maioridadehomem and sexo == 'h':
        nomevelho = nome
    if idade < 20 and sexo == 'm':
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média das idades é {médiaidade}.')
print(f'O nome do homem mais velho é {nomevelho} com {maioridadehomem} anos.')
print(f'A quantidade de mulheres menores de 20 anos é {totmulher20}.')
