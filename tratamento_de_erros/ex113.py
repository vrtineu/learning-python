# Reescreva a funçao leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitaçao de um numero de tipo invalido. Aproveite e crie também uma funçao leiaFloat() com a mesma funcionalidade.

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero real valido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


nint = leiaInt('Digite um número inteiro: ')
nfloat = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar os numeros {nint} e {nfloat}.')
