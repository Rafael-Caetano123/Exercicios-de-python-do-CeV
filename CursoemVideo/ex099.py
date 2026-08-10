"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep
def maior(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(2)
    if len(valores) == 0:
        print(f'0 - Foram informados 0 valores ao todo.')
        print(f'O maior valor inforamdo foi 0.')
        exit()
    for num in valores:
        print(f'{num} ', end='')
        sleep(0.5)
    print(f'- Foram informados {len(valores)} valores ao todo.')
    sleep(1)
    print(f'O maior valor valor informado foi o {max(valores)}.')
    sleep(1)

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
