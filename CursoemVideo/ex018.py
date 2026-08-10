"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo"""

import math
a = int(input('Digite um ângulo: '))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print ('O seno do ângulo {} é {:.2f}, o cosseno é {:.2f}, e a tagente é {:.2f}'.format(a, s, c, t))