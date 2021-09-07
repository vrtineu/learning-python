# Faça um programa que leia nome e peso de várias pessoas, guardando em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas. (> 100)
# C) Uma listagem com as pessoas mais leves. (< 70)

people = list()
data = list()

while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))

    if len(people) == 0:
        max = min = data[1]
    else:
        if data[1] > max:
            max = data[1]
        if data[1] < min:
            min = data[1]

    people.append(data[:])
    data.clear()
    answer = str(input('Quer continuar ? [Y/N] ')).lower()
    if answer in 'n':
        break

fat = list()
lean = list()

for p in people:
    if p[1] == max:
        fat.append(p[0])
    elif p[1] == min:
        lean.append(p[0])

print(
    f'Foram cadastradas {len(people)} pessoas.\nAs pessoas mais pesadas são {fat} e as mais leves são {lean}.')
