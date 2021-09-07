# Lê a largura e a altura de uma parede em metros, calcula a área e a quantidade de tinta necessária para pintá-la, sendo que cada litro de tinta pinta uma área de 2m^2.

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt
lt = area / 2

print('A dimensão da parede é {:.2f}x{:.2f}, que resulta em uma área de {:.1f}m², sendo necessário {:.1f}L de tinta para pintá-la.'.format(larg, alt, area, lt))
