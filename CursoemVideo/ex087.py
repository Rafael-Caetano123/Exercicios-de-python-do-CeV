"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l, c}: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ',end='')
    print()
print('=-' * 30)
linha2 = [matriz[1][0], matriz[1][1], matriz[1][2]]
soma_coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
soma_par = 0
for l in matriz:
    for n in l:
        if n % 2 == 0:
            soma_par += n
print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}.')
print(f'O maior valor da segunda linha é {max(linha2)}.')