# Crie um programa que leia o nome, o ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# 35 anos de contribuição
from datetime import date, datetime

dados = {}
dados['nome'] = str(input('Nome: '))
dados['ano de nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - dados['ano de nascimento']
dados['CTPS'] = int(input('CTPS (0 se não tiver): '))
del dados['ano de nascimento']

if dados['CTPS'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + \
        ((dados['ano de contratação'] + 35) - datetime.now().year)
print('-'*30)
for k, v in dados.items():
    print(f'{k} tem valor {v}.')
