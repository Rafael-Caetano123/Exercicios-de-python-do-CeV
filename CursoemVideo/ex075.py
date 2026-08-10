"""Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares digitados"""

numero_1 = int(input('Digite o 1º número: '))
numero_2 = int(input('Digite o 2º número: '))
numero_3 = int(input('Digite o 3º número: '))
numero_4 = int(input('Digite o 4º número: '))
tupla = (numero_1, numero_2, numero_3, numero_4)
quant_pares = 0
pares = 0
print('-' * 30)
print ('Valores digitados: ',end='')
for n in tupla:
    print (f'{n} ',end='')
    if n % 2 == 0:
        quant_pares += 1


if tupla.count(9) > 1:
    print (f'\nVocê digitou o número nove {tupla.count(9)} vezes')
elif tupla.count(9) == 1:
    print('\nVocê digitou o número nove 1 vez')
else:
    print('\nVocê não digitou o número 9 nenhuma vez')

if tupla.count(3) == 1:
    print(f'O valor 3 foi digitado na {tupla.index(3)+1}ª posição')
elif tupla.count(3) > 1:
    print(f'O número 3 foi digitado pel primeira vez na {tupla.index(3)+1}ª posição')
else:
    print('Você não digitou o valor 3 nenhuma vez')

if quant_pares == 1:
    print('Você digitou 1 número par: ',end='')
elif quant_pares > 1:
    print(f'Você digitou {quant_pares} números pares: ',end='')
while True:
    if numero_1 % 2 == 0:
        print(f'{numero_1} ',end='')
        pares += 1
    if numero_2 % 2 == 0:
        print(f'{numero_2} ',end='')
        pares += 1
    if numero_3 % 2 == 0:
        print(f'{numero_3} ',end='')
        pares += 1
    if numero_4 % 2 == 0:
        print(f'{numero_4} ',end='')
        pares += 1
    break
if pares == 0:
    print('Você não digitou nenhum número par')