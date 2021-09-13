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
    return f'{moeda}{num:>8.2f}'.replace('.', ',')
