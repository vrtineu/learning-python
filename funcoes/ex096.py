# Faça um programa que tenha uma função chamada área(), que receba as dimesões de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    area = largura * comprimento
    print(
        f'A área de um terreno de {largura:.1f}x{comprimento:.1f}m é de {area:.1f}m².')


print(f'{"-"*19}\nControle de Terreno\n{"-"*19}')
lar = float(input('Digite a largura(m): '))
comp = float(input('Digite a comprimento(m): '))
área(lar, comp)
