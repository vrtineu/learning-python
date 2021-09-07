# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

total = num = 0
while num != 999:
    num = int(input('Digite um número para a soma: '))
    total += num
    if num == 999:
        total -= 999
print(f'A soma de todos os valores digitado é igual a {total}')
