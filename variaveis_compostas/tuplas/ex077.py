# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
frase = ('aprender', 'python', 'fazendo', 'exercicios', 'praticar',
         'desenvolvedor', 'programador', 'curso', 'futuro', 'linguagem')

for palavra in frase:
    print(f'\nAs vogais de {palavra.upper()} são: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
