# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anonasc = int(input('Qual seu ano de nascimento(AAAA)?  '))
sexo = str(input('Qual seu sexo? [M / F] ')).lower()
idade = date.today().year - anonasc
if sexo == 'm':
    if idade < 18:
        faltam = 18 - idade
        print(f'Você ainda não está apto ao alistamento militar, ainda faltam {faltam} ano(s).')
    elif idade == 18:
        print('Você já está apto ao alistamento, vá até o posto mais próximo para realizá-lo.')
    else:
        faltam = idade - 18
        alist = date.today().year - faltam
        print(f'Você já está apto á {faltam} ano(s) ao alistamento, se ainda não o fez, é melhor ir.')
        print(f'Seu alistamento oficial foi no ano de {alist}.')
else:
    print('O alistamento militar só é obrigatório a pessoas do sexo masculino.')
