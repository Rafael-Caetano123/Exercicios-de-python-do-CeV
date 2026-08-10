"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    if resp == 'N':
        break

maior = menor = pessoas[0][1]
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

pesados = list()
leves = list()
for p in pessoas:
    if p[1] == maior:
        pesados.append(p[0])
    if p[1] == menor:
        leves.append(p[0])

print('=-' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
if len(pesados) > 1:
    print(f'As pessoas mais pesadas são: {pesados} pesando Kg{maior:.2f}')
else:
    print(f'A pessoa mais pesada é: {pesados} pesando Kg{maior:.2f}')

if len(leves) > 1:
    print(f'As pessoas mais leves são: {leves} pesando Kg{menor:.2f}')
else:
    print(f'A pessoa mais leve é: {leves} pesando Kg{menor:.2f}')