# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
num = 0
while True:
    print('-'*52)
    num = int(input('Digite o número para ver sua respectiva tabuada: '))
    if num < 0:
        break
    for i in range(0, 11):
        produto = num * i
        print(f'{i:2} x {num:2} = {produto:2}')
print('-'*52)
print('Obrigado por utilizar.')
