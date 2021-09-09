# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
listaJogadores = []
jogador = {}
gols = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(
        input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    for jogo in range(0, jogador['partidas']):
        gols.append(
            int(input(f'Quantos gols o jogador fez na partida {jogo+1}: ')))
    jogador['gols'] = gols[:]
    listaJogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    answer = str(input('Quer continuar? [Y/N] '))
    if answer in 'n':
        break
print(f"{'-'*30}\n{'Dados dos Jogadores':^30}\n{'cód':<3}  {'Nome'}    {'Gols'}{'Total':>12}\n{'-'*30}")
for i, j in enumerate(listaJogadores):
    soma = sum(j['gols'])
    print(f"{i+1:<3}{j['nome']}    {j['gols']}{soma:>12}")
print(f"{'-'*30}")
while True:
    detalhe = int(
        input('Quer ver os dados de um jogador? (999 para parar)\nCódigo do Jogador: '))
    print(f"{'-'*30}")
    if detalhe == 999:
        break
    detalhe -= 1
    print(f'Levantamento do jogador {listaJogadores[detalhe]["nome"]}: ')
    for p, g in enumerate(listaJogadores):
        print(f"No jogo {p} o jogador fez {g['gols'][p]} gols.")
print('Aplicação encerrada.')
