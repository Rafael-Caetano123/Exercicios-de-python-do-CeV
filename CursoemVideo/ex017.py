"""Faça um programa que leia o comprimento cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o seu comprimento da hipotenusa"""

from math import sqrt, trunc
c1 = int(input('Digite o comprimento do cateto adjacente: '))
c2 = int(input('Digite o comprimento do cateto oposto: '))
s1 = c1 ** 2
s2 = c2 ** 2
s3 = s1 + s2
h = sqrt(s3)
print ()
print (f'Se o cateto adjacente é {c1}, e o cateto oposto é {c2}, então a hipotenusa é igual a {trunc(h)}')