"""Crie um programa que leia vários números e colocar em uma lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida, tente novamete')
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 25)
valores.sort(reverse=True)
if len(valores) > 1:
    print(f'Você digitou {len(valores)} números')
    print(f'Os valores em ordem decrescente são {valores}')
else:
    print(f'Você digitou apenas 1 número que foi {valores[0]}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')