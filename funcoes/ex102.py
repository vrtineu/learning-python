# Crie um programa que tenha uma funçao fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: Numero a ser calculado.
    :param show: (Opcional), Mostra ou não a conta.
    :return: O valor do fatorial de um numero.
    """
    f = 1
    while n >= 1:
        if show == True:
            print(f'{n}', end='')
            print(' x ' if n > 1 else ' = ', end='')
        f *= n
        n -= 1
    return f


print(fatorial(5, show=True))
