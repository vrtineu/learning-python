# Faça um programa que leia um ano qualquer e mostra se ele é Bissexto.

from datetime import date

ano = int(input('Digite o ano(AAAA) para saber se é ou não bissexto, ou se preferir, digite 0 para utilizar o ano atual configurado em sua máquina: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
