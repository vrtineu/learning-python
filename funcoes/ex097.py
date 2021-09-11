# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
# Ex: input escreva('Olá, Mundo!')
# output:
#     ------------------
#         Olá, Mundo!
#     ------------------

def escreva(txt):
    tam = len(txt) + 4
    print(f"{'-'*tam}\n  {txt}\n{'-'*tam}")


mensagem = str(input('Mensagem: '))
escreva(mensagem)
