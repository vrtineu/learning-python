# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

num = (int(input('Número 1: ')), int(input('Número 2: ')),
       int(input('Número 3: ')), int(input('Número 4: ')))
print(num)
# print(f'O valor 9 apareceu {num.count(9)} vezes') #Resposta alternativa para a A.
nove = 0
par = ()
for numero in num:
    # A) Quantas vezes apareceu o valor 9
    if numero == 9:
        nove += 1
    # C) Quais foram os números pares
    if numero % 2 == 0:
        par += (numero,)
        print(f'Os valores pares foram: {par}')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O primeiro valor 3 está na posição: {num.index(3)}')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
