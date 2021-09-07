# Lê um número real qualquer e retorna sua parte inteira.

from math import trunc

num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é de {}.'.format(num, trunc(num)))
