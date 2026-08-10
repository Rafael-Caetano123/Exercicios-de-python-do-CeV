"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6)}
jogadores_ord = dict()
lista = []
print('Números sorteados:')
for j, n in jogadores.items():
    sleep(0.8)
    print(end='  ')
    print(f'{j} tirou {n}')
for v in jogadores.values():
    lista.append(v)
lista.sort(reverse=True)
for n in lista:
    for k, v in jogadores.items():
        if n == v:
            jogadores_ord[k] = n
print('=-' * 30)
sleep(0.8)
print('===== Ranking dos jogadores =====')
for p, (k, v) in enumerate(jogadores_ord.items()):
    print(end='   ')
    sleep(0.8)
    print(f'{p+1}º lugar: {k} com {v}')
