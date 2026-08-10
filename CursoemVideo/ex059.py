"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print('''\033[1;36m========= MENU ==========
 [ 1 ] Somar
 [ 2 ] Multiplicar
 [ 3 ] Maior
 [ 4 ] Novos números
 [ 5 ] Sair do programa
=========================\033[m''')
opção = int(input('Escolha uma das opções: '))
if opção == 5:
    print('\033[4;32mPrograma encerrado com sucesso!\033[m')
    exit()
while opção != 5:
    if opção == 1:
        print ('-' * 45)
        print (f'\033[1;32mA soma entre os números {num1} e {num2} é {num1 + num2}')
        print (f'{num1} + {num2} = {num1 + num2}\033[m')
        print ('-' * 45)
        print ('→ Se não quiser continuar digite 5 para sair do programa ←')
        opção = int(input('Escolha uma das opções: '))
        if opção == 5:
            print('\033[4;32mPrograma encerrado com sucesso!\033[m')
            exit()
    elif opção == 2:
        print('-' * 45)
        print (f'\033[1;33mA multiplicação entre {num1} e {num2} é {num1 * num2}')
        print (f'{num1} x {num2} = {num1 * num2}\033[m')
        print('-' * 45)
        print('→ Se não quiser continuar digite 5 para sair do programa ←')
        opção = int(input('Escolha uma das opções: '))
        if opção == 5:
            print('\033[4;32mPrograma encerrado com sucesso!\033[m')
            exit()
    elif opção == 3:
        maior = num1
        menor = num2
        if num2 > num1:
            maior = num2
            menor = num1
        if num1 != num2:
            print('-' * 45)
            print (f'\033[1;34mO maior número entre {num1} e {num2} é {maior}')
            print (f'{maior} > {menor}\033[m')
            print('-' * 45)
        else:
            print('-' * 45)
            print('\033[1;35mOs dois valores são iguais!\033[m')
            print('-' * 45)
        print('→ Se não quiser continuar digite 5 para sair do programa ←')
        opção = int(input('Escolha uma das opções: '))
        if opção == 5:
            print('\033[4;32mPrograma encerrado com sucesso!\033[m')
            exit()
    elif opção == 4:
        print('-' * 45)
        print ('\033[1;35m→ Escolha novos número ←')
        num1 = float(input('Digite o 1º número: '))
        num2 = float(input('Digite o 2º número: \033[m'))
        print('-' * 45)
        print('→ Se não quiser continuar digite 5 para sair do programa ←')
        opção = int(input('Escolha uma das opções: '))
        if opção == 5:
            print ('\033[4;32mPrograma encerrado com sucesso!\033[m')
    elif opção != 1 or 2 or 3 or 4 or 5:
        print('-' * 45)
        print('\033[1;31mOpção inválida!, tente novamente\033[m')
        print('→ Se não quiser continuar digite 5 para sair do programa ←')
        opção = int(input('Escolha uma das opções: '))
        if opção == 5:
            print('Programa encerrado com sucesso!')
            exit()