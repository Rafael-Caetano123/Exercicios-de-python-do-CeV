"""Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio pergunte ao usuário qual o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('=' * 40)
print('           BANCO DO PYTHON')
print('=' * 40)
valor = int(input('Qual o valor a ser sacado? R$'))
while valor <= 0:
    print('\033[1;31mValor solicitado inválido!\033[m')
    print('-' * 40)
    valor = int(input('Qual valor a ser sacado? R$'))
resto = valor
nota_50 = nota_20 = nota_10 = nota_1 = 0
while True:
    if resto >= 50:
        resto -= 50
        nota_50 += 1
        if resto == 0:
            break
    elif resto >= 20:
        resto -= 20
        nota_20 += 1
        if resto == 0:
            break
    elif resto >= 10:
        resto -= 10
        nota_10 += 1
        if resto == 0:
            break
    elif resto >= 1:
        resto -= 1
        nota_1 += 1
        if resto == 0:
            break
    else:
        break
print('Você receberá:')
if nota_50 != 0:
    print(f'Total de {nota_50} nota(s) de R$50')
if nota_20 != 0:
    print(f'Total de {nota_20} nota(s) de R$20')
if nota_10 != 0:
    print(f'Total de {nota_10} nota(s) de R$10')
if nota_1 != 0:
    print(f'Total de {nota_1} nota(s) de R$1')
print('=' * 40)
print('Volte sempre ao nosso banco :)')