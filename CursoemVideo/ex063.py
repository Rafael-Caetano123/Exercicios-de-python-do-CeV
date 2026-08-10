"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência Fibonacci."""

print('\033[1;33m=-\033[m' * 15)
print('\033[1;36m   Sequência de Fibonacci')
print('\033[1;33m=-\033[m' * 15)
termos = int(input('Quantos termos você quer mostar? '))
cont = 1
a = 0
b = 1
soma = 0
while cont < termos:
    print(f'{soma} - {b} - ' if a == 0 else f'{soma} - ', end='')
    cont += 1
    soma = a + b
    a = b
    b = soma
print('FIM')