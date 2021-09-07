# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá análisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressão = str(input('Digite uma expressão: '))
count = 0

# For percorre a expressão inteira buscando '()', se achar '(' incrementa 1 ao contador, se encontrar ')' decrementa 1 ao contador, se no final o contador terminar com 0, a expressão é válida.
for item in expressão:
    if item == '(':
        count += 1
    elif item == ')':
        count -= 1

    # Se o contador for negativo o for é interrompido, pois indica ter começado com ")"
    if count < 0:
        break

if count == 0:
    print('Expressão válida.')
elif count < 0:
    print('Expressão inválida, verifique os ")"')
elif count > 0:
    print('Expressão inválida, verifique os "("')
