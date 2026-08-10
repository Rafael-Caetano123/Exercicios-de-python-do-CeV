"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-> O primeiro valor é maior
-> O segundo valor é menor
-> Não existe valor maior, os dois são iguais"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    maior = num1
    menor = num2
    print ('O primeiro valor é o maior')
    print ('E o segundo valor é o menor')
elif num2 > num1:
    maior = num2
    menor = num1
    print ('O segundo valor é o maior')
    print ('E o primeiro valor é o menor')
else:
    print ('Não existe valor maior, os dois são iguais')