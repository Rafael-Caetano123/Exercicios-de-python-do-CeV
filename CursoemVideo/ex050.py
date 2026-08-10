"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar desconsidere-o."""

cont = 0
soma = 0
for n in range(1,7):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        soma +=num
        cont += 1
print (f'A soma de todos os {cont} números pares digitados é {soma}')