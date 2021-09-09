# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['média'] >= 7 and aluno['média'] <= 10:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(
    f'Nome do aluno: {aluno["nome"]}.\nMédia do aluno: {aluno["média"]}\nA situação do aluno é {aluno["situação"]}.')
