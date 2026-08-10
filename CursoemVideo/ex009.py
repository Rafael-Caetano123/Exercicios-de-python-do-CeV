"""Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada"""

n = int(input('Digite um número:'))
print ()
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
t10 = n*10

print(f'    Tabuada do número {n}')

print (f'({n}  x  {1} = {t1})',end='  -  ')
print (f'({n}  x  {6} = {t6})')
print (f'({n}  x  {2} = {t2})',end='  -  ')
print (f'({n}  x  {7} = {t7})')
print (f'({n}  x  {3} = {t3})',end='  -  ')
print (f'({n}  x  {8} = {t8})')
print (f'({n}  x  {4} = {t4})',end='  -  ')
print (f'({n}  x  {9} = {t9})')
print (f'({n}  x  {5} = {t5})',end='  -  ')
print (f'({n}  x {10} = {t10})')