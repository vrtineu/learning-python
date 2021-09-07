# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
posMaior = list()
posMenor = list()
for num in range(0, 5):
    # Lê 5 valores e armazena na lista.
    valores.append(int(input('Digite um número: ')))
maiorNum = max(valores)
menorNum = min(valores)
for i, v in enumerate(valores):
    if v == maiorNum:
        posMaior.append(i)
    elif v == menorNum:
        posMenor.append(i)
print(
    f'A lista digitada foi {valores}.\nO maior número é {maiorNum}, nas posições {posMaior}.\nO menor valor digitado foi {menorNum}, na posição {posMenor}.')
