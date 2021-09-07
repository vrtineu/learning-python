# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

pc = randint(0, 10)
print("Escolhi um número, sua missão é acertá-lo.")
attempt = 0
user = ''
while user != pc:
    user = int(input('Digite o número que pensei: '))
    attempt += 1
    if user < pc:
        print('É mais do que isso...')
    elif user > pc:
        print('É menos do que isso...')
print(f'Você acertou! Com {attempt} tentativa(s).')
