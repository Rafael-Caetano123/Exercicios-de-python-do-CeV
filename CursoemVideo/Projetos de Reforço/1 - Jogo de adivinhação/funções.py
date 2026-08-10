def linha():
    print('-=' * 20)

def dificuldade():
    linha()
    print('Dificuldade do jogo'.center(40))
    linha()
    print('[ 1 ] -> Fácil - (1 - 10) - 3 tent.')
    print('[ 2 ] -> Médio - (1 - 50) - 5 tent.')
    print('[ 3 ] -> Difícil - (1 - 100) - 7 tent.')
    linha()
    opc = int(input('Escolha uma opção: '))
    if opc > 3 or opc < 1:
        while opc > 3 or opc < 1:
            print('\033[1;31mERRO! digite uma opção válida\033[m')
            opc = int(input('Escolha uma opção: '))
            if opc >= 1 and opc <= 3:
                break
    linha()
    if opc == 1:
        facil()
    if opc == 2:
        medio()
    if opc == 3:
        dificil()

def facil():
    from random import randint
    comp = randint(1, 10)
    cont = 0
    while True:
        if cont != 2:
            print(f'{cont+1}ª tentativa:')
        else:
            print(f'{cont+1}ª tentativa (última chance):')
        palpite = int(input('Faça seu palpite: '))
        if palpite > 10 or palpite < 1:
            while palpite > 10 or palpite < 1:
                print('\033[1;31mERRO! de um palpite entre 1 e 10\033[m')
                linha()
                if cont != 2:
                    print(f'{cont + 1}ª tentativa:')
                else:
                    print(f'{cont + 1}ª tentativa:')
                palpite = int(input('Faça seu palpite: '))
                if palpite >= 1 and palpite <= 10:
                    break
        if palpite > comp:
            print(f'Dica: Menor que {palpite}...')
        if palpite < comp:
            print(f'Dica: Maior que {palpite}...')
        linha()
        if palpite >= 1 and palpite <= 10:
            cont += 1
        if palpite == comp:
            print('Parabéns!!! você acertou o número')
            print(f'Você acertou com {cont} tentativa(s)')
            break

        if cont == 3:
            print('Você não conseguiu acertar dessa vez')
            print(f'O número que eu tinha pensado era o {comp}')
            break


def medio():
    from random import randint
    comp = randint(1, 50)
    cont = 0
    while True:
        if cont != 4:
            print(f'{cont + 1}ª tentativa:')
        else:
            print(f'{cont + 1}ª tentativa (última chance):')
        palpite = int(input('Faça seu palpite: '))
        if palpite > 50 or palpite < 1:
            while palpite > 50 or palpite < 1:
                print('\033[1;31mERRO! de um palpite entre 1 e 50\033[m')
                linha()
                if cont != 4:
                    print(f'{cont + 1}ª tentativa:')
                else:
                    print(f'{cont + 1}ª tentativa:')
                palpite = int(input('Faça seu palpite: '))
                if palpite >= 1 and palpite <= 50:
                    break
        if palpite > comp:
            print(f'Dica: Menor que {palpite}...')
        if palpite < comp:
            print(f'Dica: Maior que {palpite}...')
        linha()
        if palpite >= 1 and palpite <= 50:
            cont += 1
        if palpite == comp:
            print('\033[1;32mParabéns!!! você acertou o número\033[m')
            print(f'Você acertou com {cont} tentativa(s)')
            break

        if cont == 5:
            print('\033[1;33mVocê não conseguiu acertar dessa vez\033[m')
            print(f'O número que eu tinha pensado era o {comp}')
            break


def dificil():
    from random import randint
    comp = randint(1, 100)
    cont = 0
    while True:
        if cont != 6:
            print(f'{cont + 1}ª tentativa:')
        else:
            print(f'{cont + 1}ª tentativa (última chance):')
        palpite = int(input('Faça seu palpite: '))
        if palpite > 10 or palpite < 1:
            while palpite > 100 or palpite < 1:
                print('\033[1;31mERRO! de um palpite entre 1 e 100\033[m')
                linha()
                if cont != 6:
                    print(f'{cont + 1}ª tentativa:')
                else:
                    print(f'{cont + 1}ª tentativa:')
                palpite = int(input('Faça seu palpite: '))
                if palpite >= 1 and palpite <= 100:
                    break
        if palpite > comp:
            print(f'Dica: Menor que {palpite}...')
        if palpite < comp:
            print(f'Dica: Maior que {palpite}...')
        linha()
        if palpite >= 1 and palpite <= 100:
            cont += 1
        if palpite == comp:
            print('\033[1;32mParabéns!!! você acertou o número\033[m')
            print(f'Você acertou com {cont} tentativa(s)')
            break

        if cont == 7:
            print('\033[1;33mVocê não conseguiu acertar dessa vez\033[m')
            print(f'O número que eu tinha pensado era o {comp}')
            break
