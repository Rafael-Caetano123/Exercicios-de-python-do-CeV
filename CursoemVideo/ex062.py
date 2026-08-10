"""Melhore o DESAFIO 061, perguntando para o usúario se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostar 0 termos."""

from time import sleep
print('\033[1;35m=-\033[m' * 16)
print('''\033[1;34m     Progressão Aritmética
            V.3.0\033[m''')
print('\033[1;35m=-\033[m'* 16)
termo_1 = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
cont = 0
total_termos = 0
while cont < 10:
    print(f'{termo_1} → ', end='')
    termo_1 += razao
    cont += 1
    total_termos += 1
print('PAUSA')
cont = 0
termo_add = int(input('Quer exibir quantos termos a mais? '))
while termo_add != 0:
    if termo_add != 0:
        cont = 0
        while cont < termo_add:
            print(f'{termo_1} → ', end='')
            termo_1 += razao
            total_termos += 1
            cont += 1
        print('PAUSA')
        termo_add = int(input('Quer exibir quantos termos a mais? '))
print('Encerrando programa...')
sleep(2)
print(f'Programa finalizado com {total_termos} termos mostrados')