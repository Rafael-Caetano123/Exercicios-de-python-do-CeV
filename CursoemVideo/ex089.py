"""Crie um programa que leia e nome duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre o boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente"""

from time import sleep
lista = list()
aluno = list()
notas = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome[:])
    notas.append(nota1)
    notas.append(nota2)
    notas.append(media)
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 30)
print('Nº  NOME          MÉDIA')
print('-' * 26)
for i,p in enumerate(lista):
    print(f'{i:<3} {p[0]:<10} {p[1][2]:>6.1f}')
print('=-' * 30)
while True:
    indice = int(input('Mostrar as notas de qual aluno? (999 interrompe) -> Nº'))
    if indice == 999:
        break
    while indice < 0 or indice > i:
        print('=-' * 30)
        print('Número inválido, tente novamente!')
        indice = int(input('Mostrar as notas de qual aluno? (999 interrompe) -> Nº'))
        if indice == 999:
            break
    if indice == 999:
        break
    print(f'As notas de {lista[indice][0]} são {lista[indice][1][0]} e {lista[indice][1][1]}, e a média é {lista[indice][1][2]:.1f}')
    print('=-' * 30)
print('=-' * 30)
print('ENCERRANDO PROGRAMA...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
