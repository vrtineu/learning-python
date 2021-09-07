# Lê o nome de uma cidade e diga se ela começa ou não com a palavra "Santo".

cidade = str(input('Digite o nome da cidade: ')).split()

print(cidade[0].lower() == 'santo')
