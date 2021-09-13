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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    count = 1
    for item in lista:
        print(f'{count} - {item}')
        count += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
