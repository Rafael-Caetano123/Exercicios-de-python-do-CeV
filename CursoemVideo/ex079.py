"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente."""

lista = list()
opcao = 'S'
while opcao == 'S':
    valor = int(input('Digite um número: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    opcao = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida tente novamente!')
        opcao = str(input('Quer continuar? [S/N] -> ')).strip().upper()
print('=-' * 25)
lista.sort()
print(f'Você digitou os valores {lista}')
