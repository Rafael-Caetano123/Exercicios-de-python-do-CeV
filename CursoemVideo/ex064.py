"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e a soma entre eles. (Desconsiderando o flag)."""

from time import sleep
print('\033[1;34m [CONDIÇÃO DE PARADA: 999]\033[m')
num = int(input('Digite um número qualquer: '))
acumulador = num
cont = 0
while num != 999:
    num = int(input('Digite um número qualquer: '))
    acumulador += num
    cont += 1
print('Encerrando Programa...')
sleep(2)
if cont > 1:
    print(f'Você digitou {cont} números, e a soma de todos eles deu {acumulador-999}')
elif cont == 1:
    print(f'Você digitou somente o número {acumulador - 999}')
else:
    print('Você não digitou nenhum número!')