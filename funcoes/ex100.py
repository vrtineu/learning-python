# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(list):
    for c in range(0, 5):
        num.append(randint(1, 10))
    print('Sorteando 5 valores para a lista: ', end='')
    for n in num:
        print(n, end=' ')
        sleep(0.2)
    print('Pronto!')


def somaPar():
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num} temos {soma}!')


num = list()
while True:
    num.clear()
    sorteia(num)
    sleep(0.5)
    somaPar()
    while True:
        answer = str(input('Quer continuar? [Y/N] ')).lower()[0]
        if answer in 'yn':
            break
        print('Erro, digite Y ou N!')
    if answer == 'n':
        break
print('Aplicação encerrada.')
