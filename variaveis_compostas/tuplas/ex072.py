# Crie um programa que tenha uma tupla totalmente preechida com contagem por extenso, de zero a vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',    'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

answer = ' '
while answer not in 'n':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Valor fora do intervalo, tente novamente.')
    print(f'Você digitou {contagem[num]}.')
    answer = str(input('Quer continuar? [Y/N] ')).strip().lower()
