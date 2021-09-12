# Faça um programa que tenha uma funçao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informaçoes:
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situaçao(opcional)
# Adicione tambem as docstrings da funçao

def notas(*notas, situacao=False):
    """
    -> Funcao para analisar nootas e situaçoes de varios alunos.
    :param notas: uma ou mais notas dos alunos (aceita varias)
    :param situaçao: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    alunos = dict()
    alunos['total'] = len(notas)
    alunos['maior'] = max(notas)
    alunos['menor'] = min(notas)
    alunos['média'] = sum(notas) / len(notas)
    if situacao == True:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif alunos['média'] >= 5:
            alunos['situação'] = 'RAZOAVEL'
        else:
            alunos['situação'] = 'RUIM'

    return alunos


resp = notas(7, 6, 8, 9, situacao=True)
print(resp)
help(notas)
