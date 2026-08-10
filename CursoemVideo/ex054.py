"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantos já são maiores."""

from datetime import datetime
ano_atual = datetime.now().year
contador18 = 0
contador = 0
for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = ano_atual - nascimento
    if idade >= 18:
        contador18 += 1
    else:
        contador += 1
if contador18 == 7:
    print (f'Todas as {contador18} pessoas do grupo são maiores de idade')
elif contador == 7:
    print (f'Todas as {contador} pessoas do grupo são menores de idade')
else:
    print(f'Neste grupo {contador18} pessoas são maiores de idade\ne as outras {contador} pessoas são menores de idade')