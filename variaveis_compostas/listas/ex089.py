# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
data = list()

while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Nota 1: ')))
    data.append(float(input('Nota 2: ')))
    alunos.append(data)
    answer = ' '
    answer = str(input('Quer continuar? [Y/N] ')).lower()
    if answer in 'n':
        break

print(f'{"="*50}\n{"Nº":<12}{"Alunos":^25}{"Média":>12}\n{"="*50}')
count = 1
for i in alunos:
    print(f'{count:.<12}{i[0]:.^25}{(i[1]+i[2])/2:.>12}')
    count += 1

while True:
    dados = int(
        input('Quer ver os dados de um aluno? (999 para parar)\nAluno: '))
    dados -= 1
    if dados == 999:
        break
    print(
        f'Dados do aluno {alunos[dados][0]}: {alunos[dados][1]}, {alunos[dados][2]}')
