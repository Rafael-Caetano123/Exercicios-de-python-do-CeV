from random import randint
from time import sleep
from rich import print
from rich.table import Table

def linha():
    print('-=' * 20)

def jogo():
    jog_pont = 0
    comp_pont = 0
    while True:
        linha()
        print('Jogo de Jokempô'.center(40))
        linha()
        print('[ 1 ] - Pedra')
        print('[ 2 ] - Papel')
        print('[ 3 ] - Tesoura')
        linha()
        comp  = randint(1, 3)
        while True:
            try:
                jogador = int(input('Escolha uma opção: '))
                if jogador > 3 or jogador < 1:
                    print('[red]ERRO! digite uma opção válida[/]')
                    continue
                break
            except (TypeError, ValueError):
                print('[red]ERRO! escolha uma opção válida[/]')
        linha()
        lista = ['JO', 'KEM', 'PÔ']
        for i in lista:
            sleep(1)
            print(f'[italic blue]{i}[/]', end=' ')
        print()
        if jogador == 1 and comp == 3:
            jog_pont += 1
            print('[green]Você Ganhou!!!')
            print('Você jogou pedra 🪨')
            print('E o computador jogou tesoura ✂️')
        elif jogador == 1 and comp == 2:
            comp_pont += 1
            print('[red]Você Perdeu[/]')
            print('Você jogou pedra 🪨')
            print('E o computador jogou papel 📄')
        elif jogador == 1 and comp == 1:
            print('[yellow]Empatou![/]')
            print('Você e o jogador jogaram pedra 🪨')
        elif jogador == 2 and comp == 1:
            jog_pont += 1
            print('[green]Você Ganhou!!![/]')
            print('Você jogou papel 📄')
            print('E o computador jogou pedra 🪨')
        elif jogador == 2 and comp == 3:
            comp_pont += 1
            print('[red]Você Perdeu[/]')
            print('Você jogou papel 📄')
            print('E o computador jogou ✂️')
        elif jogador == 2 and comp == 2:
            print('[yellow]Empatou![/]')
            print('Você e o computador jogaram papel 📄')
        elif jogador == 3 and comp == 2:
            jog_pont += 1
            print('[green]Você Ganhou!![/]')
            print('Você jogou tesoura ✂️')
            print('E o computador jogou 📄')
        elif jogador == 3 and comp == 1:
            comp_pont += 1
            print('[red]Você Perdeu[/]')
            print('Você jogou tesoura ✂️')
            print('E o computador jogou 🪨')
        elif jogador == 3 and comp == 3:
            print('[yellow]Empatou![/]')
            print('Você e o computador jogaram tesoura ✂️')
        tabela = Table(title='[italic]Pontuação[/]', width= 35)
        tabela.add_column('', justify='center', style='cyan')
        tabela.add_column('[yellow]Jogador[/]', justify='center', style='blue')
        tabela.add_column('[yellow]Computador[/]', justify='center', style='blue')
        tabela.add_row('[green]Pontos[/]', f'{jog_pont}', f'{comp_pont}')
        linha()
        opc = str(input('Quer jogar novamente? [S/N] -> ')).strip().upper()
        if opc != 'S' and opc != 'N':
            while opc != 'S' and opc != 'N':
                print('[red]ERRO! digite uma opção válida[/]')
                opc = str(input('Quer jogar novamente? [S/N] -> ')).strip().upper()
        if opc == 'S':
            continue
        if opc == 'N':
            linha()
            print(tabela)
            break
