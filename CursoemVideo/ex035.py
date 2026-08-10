"""Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo."""

print ('\033[0;33m-\033[m' * 24)
print ('\033[1;36mAnalisador de Triângulos\033[m')
print ('\033[0;33m-\033[m' * 24)
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
if a + b > c and a + c > b and b + c > a:
    print ('\033[4;32mEsses valores PODEM FORMAR triândulo!')
else:
    print ('\033[4;31mEsses valores NÃO PODEM FORMAR triângulo!')