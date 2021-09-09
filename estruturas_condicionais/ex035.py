# Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.

from time import sleep

r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))

print('Será que essas medidas podem formar um triângulo?')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
