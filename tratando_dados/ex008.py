# Lê o valor em metros, e exibe em centímetros e milímetros.

metros = float(input('Digite o valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('O valor em metros é {}m, em centímetro é {}cm e em milímetros é {}mm'.format(metros, cm, mm))
print('O mesmo valor em quilometros é {}km, hectômetros {}hm, decâmetros {}dam e decímetros {}dm.'.format(km, hm, dam, dm))
