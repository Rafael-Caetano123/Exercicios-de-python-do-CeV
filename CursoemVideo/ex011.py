"""Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²"""

a = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
ar = a * l
t = ar / 2
print (f'Sua parede tem a dimensão de {a:.2f} x {l:.2f} e sua área é de {ar:.2f}m²')
print (f'Para pintar essa parede, você precisará de {t:.2f}L de tinta.')