"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

nome = str(input('Digite o nome de uma pessoa: ')).strip()
a = nome.title()
b = 'Silva' in a
print (f'O nome "{nome}" contém "SILVA" no nome? ')
print (b)