# Faça um programa que tenha uma função chamada contador() que receba três parametros: inicio, fim e passo e realiza a contagem. Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:  # Se o passo for 0, passo recebe 1
        passo = 1
    if inicio < fim and fim > 0:
        fim += 1
    elif inicio > fim:
        fim -= 1

    # Inicio eh maior do que o final, o passo tem que ser menor que 0
    if inicio > fim:
        if passo < 0:
            for c in range(inicio, fim, passo):
                print(c, end=' ')
                sleep(0.1)
            print('Fim')
        elif passo > 0:  # Se o passo for positivo passo = -passo
            passo = passo * (-1)
            for c in range(inicio, fim, passo):
                print(c, end=' ')
                sleep(0.1)
            print('Fim')

    # Final eh maior do que o inicio, o passo tem que ser maior que 0
    if fim > inicio:
        if passo > 0:
            for c in range(inicio, fim, passo):
                print(c, end=' ')
                sleep(0.1)
            print('Fim')
        if passo < 0:  # Se o passo for negativo, passo = +passo
            passo = passo * (-1)
            for c in range(inicio, fim, passo):
                print(c, end=' ')
                sleep(0.1)
            print('Fim')


def linha():
    print('~='*14)


# Programa principal
linha()
print('Contagem de 0 a 10:')
contador(0, 10, 1)
linha()
print('Contagem de 10 a 0:')
contador(10, 0, 1)
linha()
print('Contagem Personalizada')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
print()
linha()
