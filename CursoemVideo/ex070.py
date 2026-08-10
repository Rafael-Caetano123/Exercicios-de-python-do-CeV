"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato."""

print('\033[1;32m=-\033[m' * 15)
print('\033[1;36m       LOJA DO PYTHON\033[m')
print('\033[1;32m=-\033[m' * 15)
total = produto_1000 = cont = 0
nome_produto_barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    valor_produto = float(input('Preço do produto: R$'))
    total += valor_produto
    cont += 1
    if valor_produto > 1000:
        produto_1000 += 1
    if cont == 1:
        valor_produto_barato = valor_produto
        nome_produto_barato = produto
    if valor_produto < valor_produto_barato:
        valor_produto_barato = valor_produto
        nome_produto_barato = produto
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp not in 'SN':
        print('Resposta inválida')
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    print('-' * 30)
    if resp == 'N':
        break
print('\033[1;33m============ DADOS DA COMPRA ============\033[m')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produto_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato comprado foi {nome_produto_barato} que custou R${valor_produto_barato:.2f}')