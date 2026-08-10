from rich import print

def linha():
    print('-=' * 20)

def caixa():
    linha()
    print('Caixa Eletrônico'.center(40))
    linha()
    while True:
        try:
            saque = int(input('Qual o valor a ser sacado? R$'))
            if saque < 0:
                print('[red]ERRO! digite umm valor válido[/]')
                continue
            break
        except (ValueError, TypeError):
            print('[red]ERRO! digite um valor válido[/]')

    ced_1 = ced_10 = ced_20 = ced_50 = 0

    while saque > 0:
        if (saque / 50) >= 1:
            ced_50 += 1
            saque -= 50
        elif (saque / 20) >= 1:
            ced_20 += 1
            saque -= 20
        elif (saque / 10) >= 1:
            ced_10 += 1
            saque -= 10
        else:
            ced_1 += 1
            saque -= 1

    linha()
    print('Você receberá:')
    if ced_50 > 0:
        print(f'[italic yellow]Total de {ced_50} notas de R$50,00[/]')
    if ced_20 > 0:
        print(f'[italic yellow]Total de {ced_20} notas de R$20,00[/]')
    if ced_10 > 0:
        print(f'[italic yellow]Total de {ced_10} notas de R$10,00[/]')
    if ced_1 > 0:
        print(f'[italic yellow]Total de {ced_1} notas de R$1,00[/]')
    linha()
    print(f'[green]Volte sempre ao nosso banco :)[/]')
