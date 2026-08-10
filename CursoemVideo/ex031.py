"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

d = int(input('Digite a distância da viagem em Km: '))
if d <= 200:
    print (f'O preço da passagem será de R${0.50 * d:.2f}')
else:
    print (f'O preço da passagem será de R${0.45 * d:.2f}')