# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter

resultadoJogo = {'jogador 1': randint(1, 6),
                 'jogador 2': randint(1, 6),
                 'jogador 3': randint(1, 6),
                 'jogador 4': randint(1, 6)
                 }
ranking = []

print('Resultado dos dados: ')
for k, v in resultadoJogo.items():
    print(f'O dado do {k} deu... {v}!')

print('Ranking dos jogadores:')
ranking = sorted(resultadoJogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}º colocado é o {v[0]} com o dado {v[1]}.')
