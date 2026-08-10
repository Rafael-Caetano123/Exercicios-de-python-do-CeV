def linha():
    print('-=' * 20)

def sistema():
    from rich import print
    from rich.panel import Panel
    from rich.table import Table

    turma = list()
    while True:
        aluno = dict()
        enunciado = Panel('[yellow]Sistema de Notas[/]'.center(45), width=40, style='blue')
        print(enunciado)
        aluno["nome"] = str(input('Nome do aluno: ')).strip().title()
        if aluno["nome"] == '' or aluno["nome"].isalpha() == False:
            while aluno["nome"] == '' or aluno["nome"].isalpha() == False:
                print('[red]ERRO! digite um nome válido[/]')
                linha()
                aluno["nome"] = str(input('Nome do aluno: ')).strip().title()
        linha()
        while True:
            try:
                aluno["nota_1"] = float(input('1ª nota: '))
                break
            except (ValueError, TypeError):
                print('[bold red]ERRO! digite uma nota válida[/]')
                linha()
        linha()
        while True:
            try:
                aluno["nota_2"] = float(input('2ª nota: '))
                break
            except (ValueError, TypeError):
                print('[bold red]ERRO! digite uma nota válida[/]')
                linha()
        linha()
        media = (aluno['nota_1'] + aluno['nota_2']) / 2
        if media >= 7:
            aluno['situação'] = f'[green]Aprovado[/]'
        elif media < 5:
            aluno['situação'] = f'[red]Reprovado[/]'
        else:
            aluno['situação'] = f'[yellow]Recuperação[/]'
        turma.append(aluno.copy())
        aluno.clear()
        opc = str(input('Quer continuar? [S/N] -> ')).strip().upper()
        linha()
        if opc != 'S' and opc != 'N':
            while opc != 'S' and opc != 'N':
                print('[bold red]ERRO! digite uma opção válida[/]')
                linha()
                opc = str(input('Quer continuar? [S/N] -> ')).strip().upper()
        if opc == 'S':
            continue
        else:
            break

    tabela_alunos = Table(title='[red]Lista de Alunos[/]',style='cyan')
    tabela_alunos.add_column('[blue]Nome[/]')
    tabela_alunos.add_column('[blue]1º nota[/]')
    tabela_alunos.add_column('[blue]2ª nota[/]')
    tabela_alunos.add_column('[blue]Situação[/]')
    for a in turma:
        tabela_alunos.add_row(
            a["nome"],
            str(a["nota_1"]),
            str(a["nota_2"]),
            str(a['situação'])
        )
    print(tabela_alunos)
