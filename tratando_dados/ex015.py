# Lê a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado, e mostra o preço a pagar sendo uqe o carro custa R$60 por dia e R$0.15 por km rodado.

dia = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km foram rodados? '))

total = (dia * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))
