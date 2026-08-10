"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o sálario.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime
from time import sleep
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['ano_nasc'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem) -> '))
dados['idade'] = datetime.now().year - dados['ano_nasc']

if dados['ctps'] == 0:
    print('=-' * 30)
    print('======= DADOS =======')
    sleep(1)
    print(f'Nome -> {dados["nome"]}')
    sleep(1)
    print(f'Idade de {dados["nome"]} -> {dados["idade"]}')
    sleep(1)
    print(f'Carteira de trabalho -> Não tem')
    exit()
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['sálario'] = float(input('Sálario: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - dados['ano_nasc']
    print('=-' * 30)
    print('======= DADOS =======')
    sleep(1)
    print(f'Nome -> {dados["nome"]}')
    sleep(1)
    print(f'Idade de {dados["nome"]} -> {dados["idade"]}')
    sleep(1)
    print(f'Carteira de trabalho -> {dados["ctps"]}')
    sleep(1)
    print(f'Ano de contratação -> {dados["contratação"]}')
    sleep(1)
    print(f'Sálario -> R${dados["sálario"]:.2f}')
    sleep(1)
    print(f'Aposentadoria somente com {dados["aposentadoria"]} anos de idade')