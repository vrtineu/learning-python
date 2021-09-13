def aumentar(num=0, taxa=0, format=False):
    res = num + ((num * taxa) / 100)
    return res if not format else moeda(res)


def diminuir(num=0, taxa=0, format=False):
    res = num - ((num * taxa) / 100)
    return res if not format else moeda(res)


def dobro(num=0, format=False):
    res = num * 2
    return res if not format else moeda(res)


def metade(num=0, format=False):
    res = num / 2
    return res if not format else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')


def resumo(num=0, aumento=0, redução=0):
    titulo("RESUMO DO VALOR")
    print(f'{"Preço analisado: "}{moeda(num)}')
    print(f'{"Dobro do preço: "}{dobro(num, format=True)}')
    print(f'{"Metade do preço: "}{metade(num, format=True)}')
    print(f'{aumento}{"% de aumento: "}{aumentar(num, aumento, format=True)}')
    print(f'{redução}{"% de redução: "}{diminuir(num, redução, format=True)}')


def titulo(txt):
    tam = len(txt) + 8
    print(f"{'~'*tam}\n{txt.center(tam)}\n{'~'*tam}")
