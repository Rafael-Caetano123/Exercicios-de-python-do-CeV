"""Faça um programa que leia três números e mostre qual é MAIOR e qual é o MENOR."""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
print ('-' * 20)
numeros = [n1, n2, n3]
print (f'O maior número é {max(numeros)}')
print (f'O menor número é {min(numeros)}')