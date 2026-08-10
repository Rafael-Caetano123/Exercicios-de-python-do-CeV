"""Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final mostre os 10 primeiros termos dessa progreção."""

print('\033[1;33m=-\033[m' * 10)
print('\033[1;36m    PROGRESSÃO')
print('    ARITMÉTICA\033[m')
print('\033[1;33m=-\033[m' * 10)
ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
pa = ter + raz
print('-' * 40)
print('10 primeiros termos: ')
print (ter,'-', ter + raz, end= ' - ')
for c in range(1, 9):
    pa += raz
    print(pa, end=' - ')
print ('acabou')