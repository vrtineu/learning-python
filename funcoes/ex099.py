# Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* valores):
    print('=~'*20)
    print('Analisando os valores passados...')
    maiorNum = count = 0
    for num in valores:
        if count == 0:
            maiorNum = num
        else:
            if num > maiorNum:
                maiorNum = num
        count += 1
        print(f'{num} ', end='')
    print(
        f'Foram informados {len(valores)} valores ao todo.\nO maior valor informado foi {maiorNum}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
