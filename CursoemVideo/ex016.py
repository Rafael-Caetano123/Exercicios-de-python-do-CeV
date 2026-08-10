"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
Ex: digite um número: 6.127. O número 6.127 tem a parte inteira 6"""

from math import trunc
num = float(input('Digite um número: '))
num2 = trunc(num)
print (f'A parte inteira do número {num} é {num2}')