"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média"""

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
s = n1+n2
m = s/2
print ('A média de nota do aluno é {:.2f}'.format(m))