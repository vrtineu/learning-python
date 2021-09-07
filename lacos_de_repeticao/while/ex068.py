# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('~='*20)
print(f'{"Par ou Impar - Game":^40}')
print('~='*20)
total = count = 0
while True:
    userParImpar = ' '
    while userParImpar not in 'pi':
        userParImpar = str(
            input('Você escolhe par ou ímpar [P/I]? ')).lower().strip()[0]
    user = int(input('Escolha um número de 1 a 10: '))
    if user >= 1 and user <= 10:
        pc = randint(1, 10)
        total = user + pc
        if total % 2 == 0:
            answer = 'p'
        else:
            answer = 'i'
        if userParImpar == answer:
            print('Player ganhou!')
            count += 1
        else:
            print('PC ganhou!')
            break
    else:
        print('Digite um número válido.')
print(f'O jogo acabou e o player teve {count} vitórias consecutivas!')
