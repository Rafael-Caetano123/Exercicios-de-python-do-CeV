"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar 'FIM' o programa se encerrará. OBS: Use cores"""

from time import sleep

def funcao():
    while True:
        print('\033[30;42m~' * 26)
        print('\033[30;42m Sistema de Ajuda PyHelp')
        print('\033[30;42m~' * 26)
        com = str(input('\033[mFunção ou Biblioteca (digite FIM para sair): ')).strip()
        if com in 'FIMfimFimfImFImfIMFiM':
            sleep(1.5)
            print('\033[30;41m~' * 23)
            print('Programa encerrado!')
            print('~' * 23)
            break
        tit = f'  Manual do comando {com}  '
        print('\033[30;44m~' * len(tit))
        print(f'\033[30;44m{tit}')
        print('\033[30;44m~' * len(tit))
        sleep(1.5)
        print('\033[30;107m')
        print(help(com))


funcao()
