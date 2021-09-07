# Converte alguma quantidade de dinheiro em dólar, considerando o dólar a R$3.27

real = float(input('Quanto quer converter? R$'))
dol = 3.27

con = real / dol

print('Com R${:.2f} você terá US${:.2f}'.format(real, con))
