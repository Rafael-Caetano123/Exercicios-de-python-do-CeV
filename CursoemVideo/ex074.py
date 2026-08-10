"""Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso mostre a listagem dos números gerados e também indique o maior e o menor valor que estão na tupla"""

from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ',end='')
for n in tupla:
    print(f'{n} ',end='')
print(f'\nMaior número sorteado: {max(tupla)}')
print(f'Menor número sorteado: {min(tupla)}')