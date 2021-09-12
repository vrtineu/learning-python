# Faça um programa que tenha uma funçao chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gols o jogador marcou? '))
if g.isnumeric():  # Método isnumeric para verificar se o numero digitado é mesmo ou não um numero
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
