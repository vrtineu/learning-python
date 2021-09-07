#Lê o preço de um produto e mostra o novo preço com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))

porc = 5
desc = preco - ((preco * porc) / 100)


print('O valor do produto é R${:.2f}, com {}% de desconto o valor irá reduzir para R${:.2f}.'.format(preco, porc, desc))
