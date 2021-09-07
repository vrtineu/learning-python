# Lê um número de 0 a 9999 e mostra na tela cada um dos dígitos separados.
#Ex: 1834
# unidade: 4
# dezena : 3
# centena : 8
# milhar : 1

numero = int(input('Digite um número de 0 a 9999: '))

print('Unidade: {}'.format((numero // 1) % 10))
print('Dezena: {}'.format((numero // 10) % 10))
print('Centena: {}'.format((numero // 100) % 10))
print('Milhar: {}'.format((numero // 1000) % 10))
