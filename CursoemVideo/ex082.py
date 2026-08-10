"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas."""

valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida tente novamente')
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    if resp == 'N':
        break
valores_par = list()
valores_impar = list()
cont = 0
while cont != len(valores):
    if valores[cont] % 2 == 0:
        valores_par.append(valores[cont])
    else:
        valores_impar.append(valores[cont])
    cont += 1
print('=-' * 25)
if len(valores) > 1:
    print(f'A lista completa é {valores}')
else:
    print(f'Você digitou apenas o número {valores}')
if len(valores_par) == 1:
    print(f'O único número par digitado foi {valores_par}')
elif len(valores_par) > 1:
    print(f'A lista pares é {valores_par}')
else:
    print('Você não digitou nenhum número par')
if len(valores_impar) == 1:
    print(f'O úncio número impar digitado foi {valores_impar}')
elif len(valores_impar) > 1:
    print(f'A lista de ímpares é {valores_impar}')
else:
    print('Você não digitou nenhum número par')