"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e a soma entre eles. (Desconsiderando o flag)."""

soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar) -> '))
    if num == 999:
        break
    soma += num
    cont += 1
if cont > 1:
    print(f'Você digitou {cont} números, e a soma entre eles foi de {soma}')
else:
    print('Você digitou somente 1 número, ou seja a soma é ele mesmo')