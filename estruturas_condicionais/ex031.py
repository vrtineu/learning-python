# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas.

distancia = float(input('Digite a distância em km da viagem: '))

if distancia <= 200:
    preço = distancia * 0.50
    print('Sua distância é inferior a 200km, então o preço será de R${:.2f}.'.format(preço))
else:
    preço = distancia * 0.45
    print('Sua viagem é superior a 200km, então será fornecido um desconto pela quilometragem, o preço será de R${:.2f}.'.format(preço))
