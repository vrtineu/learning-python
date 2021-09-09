# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

num1 = int(input('Digite o primeiro número para análise: '))
num2 = int(input('Digite o segundo número para análise: '))

if num2 > num1:
    print(f'O maior valor entre os dois é {num2}')
elif num1 > num2:
    print(f'O maior valor entre os dois é {num1}')
else:
    print('Não existe valor maior, os dois são iguais.')
