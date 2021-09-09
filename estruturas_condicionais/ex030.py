# Crie um programa que leia um número inteiro qualquer e mostra se ele é par ou ímpar.

numero = int(input('Digite um número inteiro qualquer para saber se ele é par ou ímpar: '))

print('O número {} é par.'.format(numero) if numero % 2 == 0 else 'O número {} é impar.'.format(numero))

# if numero % 2 == 0:
#     print('O numero {} é par.'.format(numero))
# else:
#     print('O número é ímpar.')
