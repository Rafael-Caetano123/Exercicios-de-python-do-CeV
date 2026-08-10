"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta"""

matriz = [[], [], []]
for c in range(3):
    matriz[0].append(int(input(f'Digite um número para a posição {0,c}: ')))
for c in range(3):
    matriz[1].append(int(input(f'Digite um número para o posição {1,c}: ')))
for c in range(3):
    matriz[2].append(int(input(f'Digite um número para a posição {2,c}: ')))
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ] ',end='')
    print()