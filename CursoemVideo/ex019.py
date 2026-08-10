"""Um professor quer sortear um de seus 4 alunos para apagar o quadro. faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido"""

from random import choice
al1 = str(input('Aluno número 1: '))
al2 = str(input('Aluno número 2: '))
al3 = str(input('Aluno número 3: '))
al4 = str(input('Aluno número 4: '))
ns = choice([al1, al2, al3, al4])
print ()
print (f'O aluno {ns} foi sorteado!')