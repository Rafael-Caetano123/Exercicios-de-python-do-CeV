"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO."""

ano = int(input('Qual ano quer analisar? Coloque 0 para o ano atual: '))
c1 = ano % 4
c2 = ano % 100
c3 = ano % 400
if c1 == 0 and c2 != 0 or c3 == 0:
    print (f'O ano {ano} é BISSEXTO')
else:
    print (f'O ano {ano} NÃO é BISSEXTO')