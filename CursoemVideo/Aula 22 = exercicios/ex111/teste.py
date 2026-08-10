"""Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando."""

from UtilidadesCEV import moeda

p = float(input('Digite o preço: R$'))
porc_aum = float(input('Aumento em porcentagem: '))
porc_red = float(input('Redução em porcentagem: '))
moeda.resumo(p, porc_aum, porc_red)
