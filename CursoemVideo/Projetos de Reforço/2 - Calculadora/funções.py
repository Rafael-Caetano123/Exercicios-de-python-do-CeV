def linha():
    print('-=' * 30)


def sistema():
    from time import sleep
    while True:
        linha()
        while True:
            try:
                num1 = float(input('Digite um número: '))
                break
            except ValueError:
                print('\033[1;31mERRO! por favor, digite um número válido\033[m')
                sleep(1)
        while True:
            try:
                num2 = float(input('Digite outro número: '))
                break
            except ValueError:
                print('\033[1;31mERRO! por favor, digite um número válido\033[m')
                sleep(1)
        linha()
        print('\033[1;35mCalculadora\033[m'.center(65))
        linha()
        print('[ 1 ] - Somar')
        print('[ 2 ] - Subtrair')
        print('[ 3 ] - Multiplicar')
        print('[ 4 ] - Dividir')
        print('[ 5 ] - Encerrar programa')
        linha()
        while True:
            try:
                opc = int(input('Escolha uma opção: '))
                break
            except ValueError:
                print('\033[1;31mERRO! por favor, digite uma opção válida\033[m')
                linha()
        if opc > 5 or opc < 1:
            while True:
                print('\033[1;31mERRO! por favor, digite uma opção válida\033[m')
                sleep(1)
                linha()
                opc = int(input('Escolha uma opção: '))
                if 5 >= opc >= 1:
                    break
        sleep(1)
        if opc == 1:
            soma(num1, num2)
        if opc == 2:
            subt(num1, num2)
        if opc == 3:
            mult(num1, num2)
        if opc == 4:
            divi(num1, num2)
        if opc == 5:
            break
        sleep(1)
    linha()
    print('Encerrando o programa...')
    sleep(2)
    print('\033[1;32mPrograma encerrado com sucesso.\033[m')
    linha()


def soma(n1, n2):
    linha()
    print('\033[1;32mSoma\033[m'.center(66))
    linha()
    r = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a {r}')
    print(f'{n1} + {n2} = {r}')


def subt(n1, n2):
    linha()
    print('\033[1;33mSubtração\033[m'.center(68))
    linha()
    r = n1 - n2
    print(f'{n1} menos {n2} é igual a {r:.1f}')
    print(f'{n1} - {n2} = {r:.1f}')


def mult(n1, n2):
    linha()
    print('\033[1;36mMultiplicação\033[m'.center(68))
    linha()
    r = n1 * n2
    print(f'{n1} vezes {n2} é igual a {r:.1f}')
    print(f'{n1} x {n2} = {r}')


def divi(n1, n2):
    linha()
    print('\033[1;34mDivisão\033[m'.center(68))
    linha()
    if n1 == 0 or n2 == 0:
        print('\033[1;31mERRO! você tentou fazer uma divisao por zero\033[m')
    else:
        r = n1 / n2
        print(f'{n1} dividido por {n2} é igual a {r:.1f}')
        print(f'{n1} / {n2} = {r}')
