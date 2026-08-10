"""Crie um programa que leia vários números inteiros pelo teclado. No final, da execução, mostre a média entre todos os valores
E qual foi o maior e menor valores lidos. O programa deve perguntar ao usúario se ele quer ou não continuar a digitar valores."""

from time import sleep
num = cont = acumulador = media = 0
lista = []
resposta = ''
while resposta != 'N':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] → ')).upper().strip()
    if resposta != 'S' and resposta != 'N':
        while resposta != 'S' and resposta != 'N':
            print('\033[31mResposta inválida! Tente novamente\033[m')
            resposta = str(input('Quer continuar? [S/N] → ')).upper().strip()
    lista.append(num)
    acumulador += num
    cont += 1
media = acumulador / cont
print('Encerrando Programa...')
sleep(2)
if cont > 1:
    print(f'Você digitou {cont} números, o maior valor lido foi {max(lista)} e o menor valor lido foi {min(lista)}')
    print(f'E a média entre os {cont} números digitados foi {media:.2f}')
else:
    print('Você digitou apenas 1 número, ou seja a média é ele mesmo')
    print('E o maior e menor número é ele mesmo')