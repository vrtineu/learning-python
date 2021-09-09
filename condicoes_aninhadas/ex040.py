# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceita nota: '))
nota4 = float(input('Digite a quarta nota: '))
média = (nota1 + nota2 + nota3 + nota4) / 4

if média < 5.0: 
    print(f'Sua média foi de {média}, seu status é: REPROVADO.')
elif média > 5.0 and média < 6.9:
    print(f'Sua média foi de {média}, seu status é: RECUPERAÇÃO.')
else:
    print(f'Sua média foi de {média}, seu status é: APROVADO.')
    print('Parabéns!')
