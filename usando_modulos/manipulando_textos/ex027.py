# Lê o nome completo de uma pessoa e mostra o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Seu primeiro nome é {} e o seu último nome é {}.'.format(nome[0], nome[len(nome) - 1]))
