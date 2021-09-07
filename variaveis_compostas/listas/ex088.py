# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

print(f'{"-"*30}\n{"Gerador de jogadas - Mega Sena":^30}\n{"-"*30}')
jogoMegaSena = list()
sorteio = list()
quantidade = int(input('Quantos jogos você quer gerar: '))
print('\nGerando jogos...\n')

for jogo in range(0, quantidade):
    while True:
        num = randint(0, 60)
        if num not in sorteio:
            sorteio.append(num)

        if len(sorteio) == 6:
            break

    sleep(0.7)
    jogoMegaSena.append(sorteio[:])
    sorteio.clear()
    print(f'Jogo {jogo + 1}: {jogoMegaSena[jogo]}')

print(f'{" BOA SORTE! ":~^30}')
