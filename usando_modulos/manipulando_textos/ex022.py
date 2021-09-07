# Lê o nome completo de uma pessoa e mostra o nome com todas as letras maiúsculas, com todas minúsculas, quantas letras ao todo sem considerar espaços e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculo fica assim: {}.'.format(nome.upper()))
print('Seu nome em minúsculo fica assim: {}.'.format(nome.lower()))

espaço = nome.split()

print('Seu nome contém {} letras.'.format(len(''.join(espaço))))
print('Seu primeiro nome tem {} letras.'.format(len(espaço[0])))
