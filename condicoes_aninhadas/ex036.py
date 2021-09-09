# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos deseja pagar? '))

prestação = casa / (tempo * 12)
limite = (salário * 30) / 100

print(f'O valor das suas prestações serão de R${prestação:.2f} e o valor limite baseado no seu salário é de R${limite:.2f}.')

if limite < prestação:
    print('Seu empréstimo foi negado, pois o valor da prestação excede o limite de 30% do seu salário.')
else:
    print(f'Seu empréstimo foi aprovado, suas prestações serão de R${prestação:.2f} e você irá pagar em {tempo * 12} meses.')
