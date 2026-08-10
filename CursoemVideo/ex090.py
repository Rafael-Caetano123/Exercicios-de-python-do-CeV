"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
nome = str(input('Nome: ')).capitalize().strip()
media = float(input(f'Média de {nome}: '))
if media >= 7:
    situacao = '\033[32mAprovado\033[m'
elif 7 > media >= 5:
    situacao = '\033[33mRecuperação\033[m'
else:
    situacao = '\033[31mReprovado\033[m'
aluno['nome'] = nome
aluno['média'] = media
aluno['situação'] = situacao
print('=-' * 20)
print(f'Nome = {aluno["nome"]}')
print(f'Média = {aluno["média"]}')
print(f'Situação -> {aluno["situação"]}')