"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'
-> Em que posição ela aparece pela primeira vez
-> Em que posição ela aparece pela última vez"""

frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')
print (f'A letra "A" aparece {a} vezes nesta frase')
b = frase.find('A')+1
print (f'A letra "A" aparece pela primeira vez na posição {b}')
c = frase.rfind('A')+1
print (f'A letra "A" aparece pela última vez na posição {c}')