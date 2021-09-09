# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador.
# O programa deve escrever na tela se o usuário venceu ou perdeu.

from random import choice
from time import sleep

print('Vou escolher um número de 0 a 5, você deve adivinhar o número que escolhi.')

resposta = choice([0, 1, 2, 3, 4, 5]) # Escolhe um número de 0 a 5.
# resposta = randint(0, 5)

tentativa = int(input('Qual número acha que eu escolhi? R: '))
print('.' * 5)
sleep(3)

# if resposta == tentativa:
#     print('Parabéns, você acertou!')
# else:
#     print('Você errou! O número que eu escolhi foi {}.'.format(resposta))
print('Parabéns, você acertou!' if tentativa == resposta else 'Você errou! O número que eu escolhi foi {}.'.format(resposta))
