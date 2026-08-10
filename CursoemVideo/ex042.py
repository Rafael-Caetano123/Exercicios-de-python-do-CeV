"""Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-> EQUILÁTERO: todos os lados iguais
-> ISÓSCELES: dois lados iguais
-> ESCALENO: todos os lados diferentes"""

from time import sleep
print ('\033[1;35m=-\033[m' * 17)
print ('\033[1;36m  Analisador de Triângulos v2.0 \033[m')
print ('\033[1;35m=-\033[m' * 17)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    vf = 'correto'
    print ('\033[1;32mAnalisando os valores...\033[m')
    sleep(2)
else:
    vf = 'incorreto'
    print ('\033[1;31mEsse valores não podem formar um triângulo!\033[m')

if vf == 'correto' and r1 == r2 and r1 == r3 and r2 == r3:
    print ('Todos os lados são iguais, será formado um triângulo EQUILÁTERO!')
elif vf == 'correto' and r1 != r2 and r1 != r3 and r2 != r3:
    print ('Todos os lados são diferentes, será formado um triangulo ESCALENO!')
elif vf == 'correto':
    print ('Este triângulo contém dois lados iguais, então será formado um triângulo ISÓSCELES!')