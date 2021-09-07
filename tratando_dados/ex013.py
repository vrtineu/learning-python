# Lê o salário e mostra o valor com 15% de aumento.

salario = float(input('Qual é o seu salário? R$'))

porcentagem = 15
aumento = (salario * 15) / 100
novosalario = salario + aumento

print('O salário atual é de R${:.2f}, com {}% de aumento o novo salário será de R${:.2f}'.format(salario, porcentagem, novosalario))
