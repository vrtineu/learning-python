# Crie um programa que tenha a funçao leiaInt(), que vai funcionar de forma semelhante a funçao input do python, so que fazendo validaçao para aceitar apenas valor numerico. Ex: n = leiaInt('Digite um n').

def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31m{n} não é um número.\033[m')
        if ok == True:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')
