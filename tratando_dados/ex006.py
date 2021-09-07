# Algoritmo que lê um número e mostra o dobro , o triplo e o quadrado.

n = float(input('Digite um número: '))

print('O dobro de {} é {} e o triplo é {}, \ne sua raiz quadrada é {:.2f}.'.format(n, (n * 2), (n * 3), (pow(n, (1 / 2)))))
