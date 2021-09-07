# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()
for count in range(0, 5):
    num = (int(input('Digite um número: ')))
    if count == 0:
        valores.insert(0, num)
    elif num > max(valores):
        valores.append(num)
    elif num < min(valores):
        valores.insert(0, num)
    else:
        if num > valores[0] and num < valores[1]:
            valores.insert(1, num)
        elif num > valores[1] and num < valores[2]:
            valores.insert(2, num)
        elif num > valores[2] and num < valores[3]:
            valores.insert(3, num)
        elif num > valores[3] and num < valores[4]:
            valores.insert(4, num)
print(f'A lista de valore digitados em ordem crescente é {valores}')
