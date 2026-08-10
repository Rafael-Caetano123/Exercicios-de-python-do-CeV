"""Faça um programa que leia o peso de 5 pessoas. No final, mostre qual o menor e o maior peso lidos."""

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O maior peso lido foi {maior}Kg')
print (f'O menor peso lido foi {menor}Kg')