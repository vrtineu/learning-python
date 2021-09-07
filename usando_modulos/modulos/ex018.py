# Lê um ângulo e retorna seu seno, cosseno e tangente.

from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo para ver seu seno, cosseno e tangente: '))

print('O ângulo {} tem o seno de {:.2f}, o consseno de {:.2f} e tangente de {:.2f}.'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
