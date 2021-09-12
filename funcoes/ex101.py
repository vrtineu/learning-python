# Crie um programa que tenha uma funçao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleiçoes.
# 18 anos obrigatório
# Acima de 65 opcional


def voto(ano_nascimento):
    from datetime import date

    idade = date.today().year - ano_nascimento
    if idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: O VOTO É OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: O VOTO É OBRIGATORIO'
    else:
        return f'Com {idade} anos: NÃO PODE VOTAR'


ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))
