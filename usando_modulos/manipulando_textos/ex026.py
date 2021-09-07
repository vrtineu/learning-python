# Lê uma frase e mostra quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra \"A\" aparece {} vezes na frase.'.format(frase.count('a')))

formatando = frase.split()

print('A letra \"A\" aparece pela primeira vez na posição {}, e pela última vez na posição {}.'.format(frase.find('a') + 1, frase.rfind('a') + 1))
