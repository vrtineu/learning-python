#Escreva um programa que pergunte o valor do salário de um funcionário e calcule o valor do seu aumentos, para salarios superiores a R$1.250.00, calcule um aumento de 10%, para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário? R$'))

if salario <= 1250:
    aumento = ((salario * 15) / 100) + salario
else:
    aumento = ((salario * 10) / 100) + salario

print(f'O seu novo salario será de R${aumento:.2f}.')
