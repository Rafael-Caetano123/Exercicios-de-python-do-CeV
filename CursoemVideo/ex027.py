"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
EX: Ana Maria de Souza
Primeiro: Ana
Último: Souza"""

nome = str(input('Digite o nome de uma pessoa: ')).strip()
a = nome.split()
print (f'Primeiro nome: "{a[0]}"')
print (f'Último nome: "{a[-1]}"')