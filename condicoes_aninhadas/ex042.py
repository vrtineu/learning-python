# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

from time import sleep

r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))

print('Será que essas medidas podem formar um triângulo?')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Esse será um triângulo EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse será um triângulo ISÓSCELES.')
    else:
        print('Esse será um triângulo ESCALENO.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
