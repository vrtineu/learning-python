# Crie um programa que mostre na tela que mostre todos os números pares que estão no intervalo entre 1 e 50.

print('Vou mostrar na tela os números pares de 1 a 50!')
for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end=' ')
print('Pronto!')
