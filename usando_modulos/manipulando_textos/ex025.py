# Lê o nome de uma pessoa e diga se tem "Silva" no nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem \"Silva\"? {}'.format('silva' in nome.lower().split()))
