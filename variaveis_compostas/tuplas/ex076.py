# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Coxinha', 1, 'Batata Frita', 5, 'Açai', 14,
            'Onion Rings', 5, 'Sorvete', 2, 'Refrigerante', 3.50)

# for produto in range(0, len(produtos)-1, 2):
#     print(f'{produtos[produto]}.............R${produtos[produto+1]}')

print(f'{"-"*40}\n{"LISTA DE PREÇOS":^40}\n{"-"*40}')

for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f'{produtos[posição]:.<30}', end='')
    else:
        print(f'R${produtos[posição]:>6.2f}')
