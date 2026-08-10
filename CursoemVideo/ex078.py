"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista."""

valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {valores}')
num_max = max(valores)
num_min = min(valores)
if valores[0] == valores[1] == valores[2] == valores[3] == valores[4]:
    print('Todos os números digitados são iguais!')
    exit()
if valores.count(max(valores)) == 1:
    print(f'O maior número digitado foi {num_max} na posição {valores.index(max(valores))}')
elif valores.count(max(valores)) > 1:
    print(f'O maior valor digitado foi {num_max} nas posições ',end='')
    for pos,v in enumerate(valores):
        if v == num_max:
            print(f'{pos}...',end='')
    print()
if valores.count(min(valores)) == 1:
    print(f'O menor número digitado foi {num_min} na posição {valores.index(min(valores))}')
elif valores.count(min(valores)) > 1:
    print(f'O menor valor digitado foi {num_min} nas posições ',end='')
    for pos, v in enumerate(valores):
        if v == num_min:
            print(f'{pos}...',end='')
