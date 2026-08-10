from rich import print

def linha():
    print('-=' * 20)

def sistema():
    linha()
    print('Contatos :telephone_receiver:'.center(60))
    linha()
    print('[ 1 ] - Adicionar contato')
    print('[ 2 ] - Mostrar contatos')
    print('[ 3 ] - Buscar contato')
    print('[ 4 ] - Remover contato')
    print('[ 5 ] - Sair do programa')
    linha()
    lista_contatos = list()
    contato = dict()
    while True:
        try:
            opc = int(input('Escolha uma opção: '))
            if opc < 1 or opc > 5:
                print('[red]ERRO! digite uma opção válida[/]')
                linha()
                continue
            else:
                break
        except (ValueError, TypeError):
            print('[red]ERRO! digite uma opção válida[/]')
            linha()


sistema()