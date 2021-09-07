# Lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e mostra o comprimento da hipotenusa.

from math import hypot

opost = float(input('Digite o cateto oposto: '))
adja = float(input('Digite o cateto adjacente: '))

print('Com o cateto oposto {} e o adjacente {} a hypotenusa será {:.2f}.'.format(opost, adja, hypot(opost, adja)))
