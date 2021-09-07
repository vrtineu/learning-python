# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
tabela = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Athletico-PR',
          'Internacional', 'Santos', 'São Paulo', 'Fluminense', 'Juventude', 'Cuiabá', 'Bahia', 'América-MG', 'Grêmio', 'Sport Recife', 'Chapecoense')
print(f'Lista de times do campeonatos: {tabela}\n{"="*20}')

# A) Apenas os 5 primeiros colocados
print('Os 5 primeiros colocados: {tabela[0:5]}\n{"="*20}')

# B) Os últimos 4 colocados da Tabela
print(f'Últimos 4 times: {tabela[16:]}\n{"="*20}')

# C) Uma lista com os times em ordem alfabética
print(f'Ordem alfabética: {sorted(tabela)}\n{"="*20}')

# D) Em que posição na tabela está o time do Chapecoense
for pos, i in enumerate(tabela):
    if i == 'Chapecoense':
        print(f'Posição do {i}: {pos + 1}\n{"="*20}')
# print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')
