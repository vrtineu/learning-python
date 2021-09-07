# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = ''
while sex != 'm' and sex != 'f':
    sex = str(input('Digite seu sexo [M/F]: ')).lower()
print('Valor aceito.')
