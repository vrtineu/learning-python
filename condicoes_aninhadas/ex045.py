# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('{:~^40}'.format(' JO KEN PO!!! '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
player = int(input('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura
Sua escolha: '''))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.2)
print('~=' * 14)
print(f'O computador escolheu {itens[pc]}')
print(f'O jogador escolheu {itens[player]}')
print('~=' * 14)
if pc == 0:  # PC ESCOLHE PEDRA
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('PLAYER VENCEU!')
    elif player == 2:
        print('PC VENCEU!')
    else:
        print('Jogada inválida.')
elif pc == 1:  # PC ESCOLHE PAPEL
    if player == 0:
        print('PC VENCEU!')
    elif player == 1:
        print('Empate!')
    elif player == 2:
        print('PLAYER VENCEU!')
    else:
        print('Jogada inválida.')
else:  # PC ESCOLHE TESOURA
    if player == 0:
        print('PLAYER VENCEU!')
    elif player == 1:
        print('PC VENCEU!')
    elif player == 2:
        print('Empate!')
    else:
        print('Jogada inválida.')
