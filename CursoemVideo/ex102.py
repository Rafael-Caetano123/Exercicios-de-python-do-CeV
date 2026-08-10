"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo do cálculo do fatorial"""

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: Mostrar o cálculo do Fatorial (opcional).
    :return: O valor do Fatorial de um número n.
    """
    for c in range(num, 0, -1):
        if c == num:
            fat = c
        else:
            fat *= c
    print(f'O fatorial de {num} é {fat}')
    if resp == 'S':
        show = True
    if show == True:
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {fat}')


# Programa Principal
n = int(input('Digite um número: '))
resp = str(input(f'Quer mostrar o cálculo fatorial de {n}? [S/N] -> ')).strip().upper()
while resp != 'S' and resp != 'N':
    print('Resposta inválida, tente novamente')
    print('-=' * 30)
    resp = str(input(f'Quer mostrar o cálculo fatorial de {n}? [S/N] -> ')).strip().upper()
print('-=' * 30)
fatorial(num= n)
print('-=' * 30)
