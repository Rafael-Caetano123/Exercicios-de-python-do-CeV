"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. US$1,00 = R$3,27"""

n1 = float(input('Quanto reais você tem na carteira? '))
d = n1/3.27
print ('você pode comprar: US${:.2f}'.format(d))