"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valore PARES sorteados pela função anterior."""

from random import randint
from time import sleep

nums_sort = list()
def sorteia():
    for c in range(5):
        nums_sort.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for num in nums_sort:
        print(f'{num} ', end='')
        sleep(0.5)
    print('Fim!')

def somapar():
    soma_par = 0
    for num in nums_sort:
        if num % 2 == 0:
            soma_par += num
    print(f'Somando todos os números pares entre {nums_sort} o total é {soma_par}')


# Programa principal
sorteia()
somapar()
