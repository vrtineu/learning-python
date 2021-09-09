# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40 Obesidade mórbida

peso = float(input('Digite o peso(kg): '))
altura = float(input('Digite a altura(m): '))
imc = peso / (altura ** 2)

print(f'O IMC é de {imc:.1f}')

if imc < 18.5:
    print('Situação: ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Situação: PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Situação: SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Situação: OBESIDADE')
else:
    print('Situação: OBESIDADE MÓRBIDA')
