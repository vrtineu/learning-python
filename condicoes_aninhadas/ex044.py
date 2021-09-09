# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

preço = float(input('Informe o valor do produto: R$'))
opção = int(input('''Informe o método de pagamento:
[1] à vista (dinheiro/cheque) 
[2] à vista no cartão 
[3] se for parcelar no cartão
Sua opção: '''))

if opção == 1:
    valor = preço - ((preço * 10) / 100)
    print(f'O preço do produto será de R${valor:.2f}, pois seu método de pagamento lhe deu 10% de desconto.')
elif opção == 2:
    valor = preço - ((preço * 5) / 100)
    print(f'O preço do produto será de R${valor:.2f}, pois seu método de pagamento lhe deu 5% de desconto.')
elif opção == 3:
    parcelas = int(input('Informe em quantas parcelas deseja pagar: '))
    if parcelas == 1:
        valor = preço - ((preço * 5) / 100)
        totalparc = valor / parcelas
        print(f'O preço do produto será de R${valor:.2f}, pois seu método de pagamento lhe deu 5% de desconto, e suas parcelas serão de R${totalparc:.2f}.')
    elif parcelas == 2:
        totalparc = preço / parcelas
        print(f'O preço do produto será de R${preço:.2f}, e suas parcelas serão de R${totalparc:.2f}.')
    else:
        valor = preço + ((preço * 20) / 100)
        totalparc = valor / parcelas
        print(f'O preço do produto será de R${valor:.2f}, pois seu método de pagamento acrescenta 20% de juros por conta do número de parcelas, e com isso suas parcelas serão de R${totalparc:.2f}.')
