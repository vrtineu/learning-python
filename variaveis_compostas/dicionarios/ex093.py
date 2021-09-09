# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(
    input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for jogo in range(0, jogador['partidas']):
    gols.append(
        int(input(f'Quantos gols o jogador fez na partida {jogo+1}: ')))
jogador['gols'] = gols[:]
print(f"{'-'*30}\n{jogador}\n{'-'*30}")
print(
    f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.\n{'-'*30}")
jogador['total'] = sum(jogador["gols"])
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print(f"{'-'*30}")
for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'{"-"*30}\nA soma foi de {jogador["total"]} gols.')
