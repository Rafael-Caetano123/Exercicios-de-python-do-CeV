def verific_nome(texto):
    return texto.replace(' ', '').isalpha()

def cadastro():
    from time import sleep
    open('pessoas.txt', 'a').close()
    while True:
        print('-=' * 19)
        print('MENU PRINCIPAL'.center(38))
        print('-=' * 19)
        print('\033[1;33m1 - \033[m\033[1;34mVer pessoas cadastradas\033[m')
        print('\033[1;33m2 - \033[m\033[1;34mCadastrar nova pessoa\033[m')
        print('\033[1;33m3 - \033[m\033[1;34mApagar lista de pessoas')
        print('\033[1;33m4 - \033[m\033[1;34mSair do sistema\033[m')
        print('-=' * 19)

        try:
            opc = int(input('\033[1;32mSua opção: \033[m'))

        except ValueError:
            print('\033[1;31mERRO: por favor, digite uma opção válida!\033[m')
            continue

        if opc == 1:
            print('-=' * 19)
            print('PESSOAS CADASTRADAS'.center(38))
            print('-=' * 19)
            arquivo = open('pessoas.txt', 'r')
            linhas = arquivo.readlines()
            if not linhas:
                print('Nenhuma pessoa cadastrada...')
            else:
                for linha in linhas:
                    print(linha.strip().replace(';', ''))
            arquivo.close()
            print('-=' * 19)


        elif opc == 2:
            print('-=' * 19)
            print('NOVO CADASTRO'.center(38))
            print('-=' * 19)
            dados = list()
            nome = str(input('Nome: ')).strip().title()
            nome_ver = verific_nome(nome)
            while not nome_ver:
                print('-=' * 19)
                print('\033[1;31mERRO: por favor, digite um nome válido!\033[m')
                nome = str(input('Nome: ')).strip().title()
                nome_ver = verific_nome(nome)
            dados.append(nome.ljust(30, '.'))

            while True:
                try:
                    idade = int(input('Idade: '))
                    dados.append(idade)
                    break
                except ValueError:
                    print('\033[1;31mERRO: por favor, digite uma idade válida!\033[m')

            print('-=' * 19)
            arquivo = open('pessoas.txt', 'a')
            arquivo.write(f'{dados[0]};{dados[1]} anos\n')
            arquivo.close()
            dados.clear()

        elif opc == 3:
            arquivo = open('pessoas.txt', 'w')
            arquivo.close()
            print('Lista de pessoas apagada.')

        elif opc == 4:
            print('-=' * 19)
            print('\033[1;33mENCERRANDO PROGRAMA...')
            sleep(2)
            print('Muito obrigado, volte sempre!\033[m')
            break

        else:
            print('-=' * 19)
            print('\033[1;31mERRO: por favor, digite uma opção válida!\033[m')