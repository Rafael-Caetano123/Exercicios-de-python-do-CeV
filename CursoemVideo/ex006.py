"""Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada"""

n1 = int(input('Digite um número:'))

d = n1*2
print (f'Dobro de {n1} é: {d}')

t = n1*3
print (f'Triplo de {n1} é: {t}')

rq = n1**(1/2)
print ('raiz quadrada de {} é: {:.3}'.format(n1, rq))