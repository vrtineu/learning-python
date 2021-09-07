# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
answer = ''
while answer != 5:
    print('=~' * 12)
    print('''O que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos valores
[5] Sair do programa''')
    answer = int(input('Sua escolha: '))
    print('=~' * 12)
    if answer == 1:
        soma = num1 + num2
        print(f'O resultado da soma é {soma}!')
    elif answer == 2:
        produto = num1 * num2
        print(f'O resultado da multiplicação é {produto}!')
    elif answer == 3:
        if num1 > num2:
            print(f'{num1} é o maior número!')
        elif num2 > num1:
            print(f'{num2} é o maior número!')
        else:
            print('Nenhum dos dois é maior.')
    elif answer == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    else:
        print('Digite um número válido.')
print('Programa encerrado.')
