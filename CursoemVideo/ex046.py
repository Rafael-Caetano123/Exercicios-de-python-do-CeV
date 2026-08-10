"""Faça um programa que mostre na tela uma contagem regressiva para o esoturo de fogos de artíficio, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""

from time import sleep
print ('\033[1;36m-=\033[m' * 15)
print ('\033[1;33m     Contagem Regressiva\033[m')
print ('\033[1;36m-=\033[m' * 15)
r = str(input('Aperte ENTER para começar '))
print ('-' * 30)
for c in range(10, 0, -1):
    print (c)
    sleep (1)
print ('🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉BUUUUMMMM🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉')