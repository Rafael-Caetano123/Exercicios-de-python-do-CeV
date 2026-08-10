"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
O nome do jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha informado corretamente."""

def ficha(nome, gols):
    print('-=' * 20)
    print(f'O jogador {nome} fez {gols} gol(s).')
    print('-=' * 20)


# Programa Principal
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: ')).strip()
if len(nome) == 0 or nome.strip() == '':
    nome = '<desconhecido>'
if len(gols) == 0 or gols not in '1234567890':
    gols = '0'
ficha(nome=nome, gols=gols)
