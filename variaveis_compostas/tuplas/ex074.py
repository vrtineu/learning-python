# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint, randrange

# num = [(randrange(0, 50)) for i in range(5)] #Essa solução não funciona, pois cria uma lista.
num = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))

print(f'Valores sorteados: {num}')
print(f'O maior valor sorteado foi {max(num)} e o menor foi {min(num)}.')

# for numero in num:
#     if numero == num[0]:
#         maiorNum = num[0]
#         menorNum = num[0]
#     if numero > maiorNum:
#         maiorNum = numero
#     if numero < menorNum:
#         menorNum = numero
# print(f'O maior número é {maiorNum} e o menor número é {menorNum}')
