# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = count = sum = 0
while True:
    num = int(input('Digite um valor inteiro (999 para encerrar): '))
    if num == 999:
        break
    sum += num
    count += 1
print(f'Você digitou {count} valores, e a soma entre eles é igual a {sum}.')
