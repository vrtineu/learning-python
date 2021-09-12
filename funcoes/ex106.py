# Faça um mini sistema que utilize o Interactive Help do python. O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra "fim", o programa se encerrara.
c = ('\033[m',         # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print(f"{'~'*tam}\n  {txt}\n{'~'*tam}\n")
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Digite uma função ou biblioteca > ')).strip()
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('OBRIGADO POR UTILIZAR', 1)
