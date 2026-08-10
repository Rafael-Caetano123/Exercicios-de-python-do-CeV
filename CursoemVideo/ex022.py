"""Crie um programa que leia o nome completo de uma pessoa de uma pessoa e mostre:
O nome com todas as letras maiúsuculas
O nome com todas as letras minúsculas
Quantas letras tem no total (sem considerar espaços)
Quantas letras tem o primeiro nome"""

nome = input('Digite um nome completo: ')
maiusculo = nome.upper()
print (f'Nome completo maiúsculo: {maiusculo}')
minusculo = nome.lower()
print (f'Nome completo minúsculo: {minusculo}')
separar = ''.join(nome)
juntar = separar.replace(' ', '')
letras = len(juntar)
print (f'O nome completo contém {letras} letras')
nome1 = nome.split()
nome1b = len(nome1[0])
print (f'O primeiro nome contém {nome1b} letras')