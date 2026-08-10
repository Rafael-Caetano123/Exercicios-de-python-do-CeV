"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input()
mas com uma validação de dados para aceitar apenas valores que sejam monetários."""

from UtilidadesCEV import moeda, dado

p = dado.leiadinheiro('Digite o preço: R$')
porc_aum = float(input('Aumento em porcentagem: '))
porc_red = float(input('Redução em porcentagem: '))
moeda.resumo(p, porc_aum, porc_red)
