"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da progressão usando a estrutura while"""

print('\033[1;35m=-\033[m' * 16)
print('''\033[1;34m     Progressão Aritmética
            V.2.0\033[m''')
print('\033[1;35m=-\033[m'* 16)
termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
contador = 0
while contador < 10:
    print(f'{termo} → ', end='')
    contador += 1
    termo += razao
print(f'FIM')