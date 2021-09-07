# Lê as duas notas de um aluno e mostra a média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2

print('A primeira nota é {:.1f}, a segunda nota é {:.1f} e a média entre as duas é {:.1f}'.format(n1, n2, média))
