# Modifique as funçoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou nao formatado pela funçao moeda(), desenvolvida no desafio 108.
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, format=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,format=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, format=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, format=True)}')
