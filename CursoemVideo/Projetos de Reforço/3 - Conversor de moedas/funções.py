def linha():
    print('-=' * 30)

def conversor():
    from time import sleep
    while True:
        linha()
        print('Conversor de Moedas'.center(60))
        linha()
        print('[ 1 ] - Real para Dólar (R$ -> US$)')
        print('[ 2 ] - Dólar para Real (US$ -> R$)')
        print('[ 3 ] - Encerrar programa')
        linha()
        while True:
            try:
                opc = int(input('Escolha uma opção: '))
                if opc < 1 or opc > 3:
                    while True:
                        print('\033[1;31mERRO! por favor, digite uma opção válida\033[m')
                        linha()
                        opc = int(input('Escolha uma opção: '))
                        if 1 <= opc <= 3:
                            break
                break
            except (ValueError, TypeError):
                print('\033[1;31mERRO! por favor, digite uma opção válida\033[m')
                linha()
        if opc == 1:
            conv1()
        if opc == 2:
            conv2()
        if opc == 3:
            linha()
            print('Encerrando programa...')
            sleep(2)
            print('\033[1;32mPrograma encerrado com sucesso!\033[m')
            break


def conv1():
    while True:
        try:
            num = float(input('Digite o valor: R$'))
            valor_conv = num / 5
            break
        except:
            print('\033[1;31mERRO! por favor, digite um valor válido\033[m')
    linha()
    print(f'R${num:.2f} convertido para dólares é igual a US${valor_conv:.2f}')
    print(f'R${num:.2f} -> US${valor_conv:.2f}')

def conv2():
    while True:
        try:
            num = float(input('Digite o valor: US$'))
            valor_conv = num * 5
            break
        except:
            print('\033[1;31mERRO! por favor, digite um valor válido\033[m')
    linha()
    print(f'US${num:.2f} convertido para reais é igual a R${valor_conv:.2f}')
    print(f'US${num:.2f} -> R${valor_conv:.2f}')