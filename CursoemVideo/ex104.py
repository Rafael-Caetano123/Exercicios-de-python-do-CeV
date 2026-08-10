"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do Python
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n:')"""


def leiaint(msg):
    valido = False
    entrada = str(input(msg)).strip()
    cont = 0
    while not valido:
        cont = entrada.count(',') + entrada.count('.')
        if entrada.isalpha() or entrada == '' or cont != 0:
            print('\033[31mERRO: digite um número inteiro válido!\033[m')
            entrada = str(input(msg)).strip()
        else:
            valido = True
            return entrada


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
