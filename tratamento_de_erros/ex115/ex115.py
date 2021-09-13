# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opçoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    answer = menu(['Ver pessoas cadastradas',
                   'Cadastrar novas pessoas', 'Sair do Sistema'])
    if answer == 1:
        # opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif answer == 2:
        # opçao para cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        # opção para sair do sistema.
    elif answer == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        # caso não for digitado nenhuma opção valida.
        print('ERRO! Digite uma opção válida')
    sleep(1)
