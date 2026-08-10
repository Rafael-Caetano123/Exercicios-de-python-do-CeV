"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"."""

cidade = str(input('Digite o nome de uma cidade: ')).strip()
a = cidade.split()
b = a[0].title()
c = 'Santo' in b
print (f'a cidade "{cidade}" começa com SANTO?' )
print (c)