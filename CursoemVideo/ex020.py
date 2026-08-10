"""O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos 4 alunos e mostre a ordem sorteada"""

from random import shuffle
al1 = str(input('Aluno número 1: '))
al2 = str(input('Aluno número 2: '))
al3 = str(input('Aluno número 3: '))
al4 = str(input('Aluno número 4: '))
lista =  [al1,  al2,  al3,  al4]
shuffle(lista)
print ('A ordem de apresentação dos trabalhos será a seguinte:')
print (lista)