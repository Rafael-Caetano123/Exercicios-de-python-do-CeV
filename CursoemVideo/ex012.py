"""Faça um algoritimo que leia o preço de um prouto e mostre seu novo preço, com 5% de desconto"""

p = float(input('Digite o preço de um produto: R$'))
d = 5
c1 = d / 100
c2 = c1 * p
c3 = p - c2

print (f'O valor do produto com 5% de desconto será de: R${c3:.2f}')