# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado. Crie uma funçao chamada leiaDinheiro() que seja capaz de funcionar como a funçao input(), mas com uma validaçao de dados para aceitar apenas valores que sejam monetarios.
from utilidadescev import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
