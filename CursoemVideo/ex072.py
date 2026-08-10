"""Cire um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20), e mostrá-lo por extenso"""

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')

cont = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    cont += 1
    print (f'Você digitou o número {extenso[num]}')
    resp = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    while resp != 'S' and resp != 'N':
        print ('Resposta inválida, tente novamente!')
        resp = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    if resp == 'N':
        break
print(f'Você digitou {cont} números')