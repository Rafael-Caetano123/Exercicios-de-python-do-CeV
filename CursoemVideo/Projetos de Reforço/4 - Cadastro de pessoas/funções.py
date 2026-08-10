def linha():
    print('-=' * 20)


def sistema():
    linha()
    print('Cadastro de Pessoas'.center(40))
    linha()
    cadastro()

def cadastro():
    tot_pes = 0
    mulheres = list()
    soma_idades = 0
    pessoa = dict()
    lista_pessoas = list()
    while True:
        nome = str(input('Nome: ')).strip().title()
        if nome == '' or nome.replace(' ', '').isalpha() == False:
            while nome == '' or nome.replace(' ', '').isalpha() == False:
                print('ERRO! digite um nome válido')
                linha()
                nome = str(input('Nome: ')).strip().title()
        pessoa['nome'] = nome

        while True:
            try:
                idade = int(input('Idade: '))
                pessoa['idade'] = idade
                soma_idades += idade
                break
            except (ValueError, TypeError):
                print('ERRO! digite uma idade válida')
                linha()

        sexo = str(input('Sexo: [M/F] -> ')).strip().upper()
        if sexo != 'M' and sexo != 'F' or sexo == '' or sexo.isalpha() == False:
            while sexo != 'M' and sexo != 'F' or sexo == '' or sexo.isalpha() == False:
                print('ERRO! digite um sexo válido')
                linha()
                sexo = str(input('Sexo: [M/F] -> ')).strip().upper()
        pessoa['sexo'] = sexo
        if sexo == 'F':
            mulheres.append(nome)

        lista_pessoas.append(pessoa.copy())
        pessoa.clear()
        tot_pes += 1

        linha()
        opc = str(input('Quer continuar? [S/N] -> ')).strip().upper()
        linha()
        if opc != 'S' and opc != 'N' or opc == '' or opc.isalpha() == False:
            while opc != 'S' and opc != 'N' or opc == '' or opc.isalpha() == False:
                print('ERRO! digite uma opção válida')
                linha()
                opc = str(input('Quer continuar? [S/N] -> ')).strip().upper()
        if opc == 'N':
            media_idades = soma_idades / tot_pes
            acima_media = list()
            for p in lista_pessoas:
                if p['idade'] > media_idades:
                    acima_media.append(p['nome'])
            print(f'Ao todo foram cadastradas {tot_pes} pessoa(s).')
            print(f'A média de idade do grupo é de {media_idades:.0f} anos.')
            if tot_pes == 1:
                print(f'A única pessoa cadastrada do grupo foi o(a) {lista_pessoas[0]["nome"]}.')
            if len(mulheres) > 0:
                print(f'As mulheres cadastradas foram ',end='')
                print(mulheres)
            if len(acima_media) > 0:
                print(f'Lista de pessoas com a idade acima da média do grupo: ',end='')
                print(acima_media)
            break
