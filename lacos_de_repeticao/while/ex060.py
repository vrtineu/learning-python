# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

# from math import factorial
num = int(input('Digite um número para ver seu fatorial: '))
# print(factorial(num))
mult = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while mult >= 1:
    print(f'{mult}', end='')
    print(' x ' if mult > 1 else ' = ', end='')
    fatorial *= mult
    mult -= 1
print(f'{fatorial}.')
