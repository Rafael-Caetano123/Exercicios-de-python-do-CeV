"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número: '))
tot = 0
for primo in range(1, num+1, 1):
    if num % primo == 0:
        tot += 1
        print(f'\033[32m{primo}\033[m',end= ' ')
    else:
        print(f'\033[31m{primo}\033[m',end= ' ')
if tot == 2:
    print(f'\nO número {num} foi divido {tot} vezes')
    print('E por isso ele é um número primo')
else:
    print(f'O número {num} foi divido {tot} vezes')
    print('E por isso ele não é um número primo')