# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite o número que quer ver a respectiva tabuada: '))
for c in range(1, 11):
    print(f'{num:2} x {c:2}: {num * c}')
