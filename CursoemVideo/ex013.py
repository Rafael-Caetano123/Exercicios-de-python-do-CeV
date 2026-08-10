"""Faça um algoritimo que leia o sálario de um funcionário e mostre o seu novo sálario com 15% de aumento"""

s = float(input('Digite o sálario do funcionário: '))
c1 = 15 / 100
c2 = (c1 * s) + s

print (f'O sálario do funcionário que ganhava {s:.2f} com 15% de aumento, passa a receber R${c2:.2f}')