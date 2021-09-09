# A Confederação Nacional de Notação precisa de um programa que leia o nascimento de um atleta e mostre sua categoria, de acordo com idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima de 20 anos: Master

from datetime import date

anonasc = int(input('Digite o ano de seu nascimento (AAAA): '))
idade = date.today().year - anonasc

if idade <= 9:
    print(f'{idade} anos, a categoria é: MIRIM.')
elif idade <= 14:
    print(f'{idade} anos, a categoria é: INFANTIL.')
elif idade <= 19:
    print(f'{idade} anos, a categoria é: JUNIOR.')
elif idade <= 25:
    print(f'{idade} anos, a categoria é: SÊNIOR.')
else:
    print(f'{idade} anos, a categoria é: MASTER.')
