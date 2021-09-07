# Lê o nome de quatro alunos e mostra uma ordem sorteada.

from random import shuffle

alunos = 'Vinicius Henrique Biriba Luca'.split()

shuffle(alunos)

print(alunos)
