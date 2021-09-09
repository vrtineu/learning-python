# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

num = int(input('Digite o número que deseja realizar a coversão: '))
print('''Escolha uma das bases para fazer a conversão: 
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
conversão = int(input('Sua opção: '))

if conversão == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif conversão == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif conversão == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')
