"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção:
-> 1 para binário
-> 2 para octal
-> 3 para hexadecimal"""

print ('\033[1;35m=-\033[m' * 20)
print ('\033[1;36m         Conversor de números\033[m')
print ('\033[1;35m=-\033[m' * 20)
print ("""Escolha uma das bases para conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal""")
opção = int(input('opção: '))
print ('\033[1;35m=-\033[m' * 20)
num = int(input('Digite um número inteiro: '))
if opção == 1:
    print (f'{num} convertido para \033[33mBINÁRIO\033[m é igual a {bin(num)[2:]}')
elif opção == 2:
    print (f'{num} convertido para \033[33mOCTAL\033[m é igual a {oct(num)[2:]}')
elif opção == 3:
    print (f'{num} convertido para \033[33mHEXADECIMAL\033[m é igual a {hex(num)[2:]}')
else:
    print ('\033[1;31mOpção invalida! digite uma das três opções')