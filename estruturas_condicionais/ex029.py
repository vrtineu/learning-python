# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostrar uma mensagem dizendo que foi multado, a multa custa RS7.00 por cada km acima do limite.

velocidade = float(input('Qual foi a velocidade registrada? '))
limite = 80
if velocidade <= limite:
    print('Velocidade dentro do limite permitido.')
else:
    multa = (velocidade - limite) * 7
    print('Você ultrapassou o limite de velocidade de 80km/h e foi multado em R${:.2f}.'.format(multa))
