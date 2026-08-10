"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função."""

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação delas
    :param n: Recebe uma ou mais notas (várias notas)
    :param sit: Exibi a situação em relação as notas (parâmetro opcional)
    :return: Dicionário com informações em relação as notas
    """
    dic = {'tot_notas': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if dic["média"] >= 7:
        dic['situação'] = '\033[1;32mBoa\033[m'
    elif 7 > dic["média"] >= 5:
        dic['situação'] = '\033[1;33mRazoável\033[m'
    else:
        dic['situação'] = '\033[1;31mRuim\033[m'
    print('-=' * 30)
    print(f'Total de Notas -> {dic["tot_notas"]}')
    print(f'Maior Nota -> {dic["maior"]}')
    print(f'Menor Nota -> {dic["menor"]}')
    print(f'Média de Notas -> {dic["média"]:.1f}')
    print('-=' * 30)
    resp = str(input('Quer ver a situação em relação as notas? [S/N] -> ')).strip().upper()
    if resp != 'S' and resp != 'N':
        while resp != 'S' and resp != 'N':
            print('\033[1;31mResposta inválida, tente novamente!\033[m')
            print('-=' * 30)
            resp = str(input('Quer ver a situação em relação as notas? [S/N] -> ')).strip().upper()
    if resp == 'S':
        sit = True
    if sit == True:
        print(f'Situação das Notas -> {dic["situação"]}')
    else:
        print('Programa encerrado!')


# Programa Principal
notas(5.5, 9.5, 10, 6.5)
