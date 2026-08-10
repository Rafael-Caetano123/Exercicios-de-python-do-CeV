"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

import moedas
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentando(p, 10)}')
print(f'Reduzindo 13%, temos {moedas.reduzindo(p, 13)}')
