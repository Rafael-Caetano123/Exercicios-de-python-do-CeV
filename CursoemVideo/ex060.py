"""Faça um programa que leia um número qualquer e mostre o seu fatorial:
EX: 5! = 5x4x3x2x1 = 120"""

num = int(input('Digite um número: '))
sub = num
acumulador = 1
print(f'{num}! = ', end='')
while sub > 0:
    print(f'{sub}', end= '')
    print(' x ' if sub > 1 else ' = ', end= '')
    acumulador = acumulador * sub
    sub -= 1
print(acumulador)
print(f'\nO fatorial de {num} é {acumulador}')