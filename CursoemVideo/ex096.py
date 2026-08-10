"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de terreno retangular (largura e comprimento)
a mostre a área do terreno."""

print('-=' * 15)
print('    Controle de Terrenos')
print('-=' * 15)

def area():
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a:.1f}m²')


# Programa principal
area()