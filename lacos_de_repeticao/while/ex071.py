# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1.
print('~=' * 10)
print(f'{"CAIXA ELETRÔNICO":-^20}')
print('~=' * 10)

ced50 = ced20 = ced10 = ced1 = 0
saque = int(input('Digite o valor desejado para saque R$'))
while True:
    if saque >= 50:
        ced50 = saque // 50
        if saque % 50 == 0:
            print(f'Total de {ced50} cédulas de R$50.')
            break
        else:
            print(f'Total de {ced50} cédulas de R$50.')
            saque %= 50
    elif saque >= 20:
        ced20 = saque // 20
        if saque % 20 == 0:
            print(f'Total de {ced20} cédulas de R$20.')
            break
        else:
            print(f'Total de {ced20} cédulas de R$20.')
            saque %= 20
    elif saque >= 10:
        ced10 = saque // 10
        if saque % 10 == 0:
            print(f'Total de {ced10} cédulas de R$10.')
            break
        else:
            print(f'Total de {ced10} cédulas de R$10.')
            saque %= 10
    else:
        ced1 = saque // 1
        print(f'Total de {ced1} cédulas de R$1.')
        break
