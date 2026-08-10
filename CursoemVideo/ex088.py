"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta"""

from random import randint
from time import sleep
print('\033[1;33m=\033[m' * 30)
print('\033[1;36m      JOGO DA MEGA SENA\033[m')
print('\033[1;33m=\033[m' * 30)
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista_jogos = list()
jogo = list()
for j in range(quant_jogos):
    while len(jogo) < 6:
        num_sort = randint(1,60)
        if num_sort not in jogo:
            jogo.append(num_sort)
    lista_jogos.append(jogo[:])
    jogo.clear()
for j in range(quant_jogos):
    lista_jogos[j].sort()
print('=-' * 18)
print(f'------- SORTEANDO {quant_jogos} JOGOS -------')
sleep(1)
for j in range(quant_jogos):
    print(f'Jogo {j+1}: {lista_jogos[j]}',end='')
    print()
    sleep(1)
print('=-' * 18)
