# Conversor de temperaturas

temperatura = float(input('Digite a temperatura em Celsius: '))

fahr = (temperatura * 1.8) + 32
kel = temperatura + 273

print('A temperatura de {}ºC corresponde a {}ºF e a {}K.'.format(temperatura, fahr, kel))
