# Crie um modulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), dobro() e metade(). Faça tambem um programa que importe esse modulo e use algumas dessas funçoes.

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')
