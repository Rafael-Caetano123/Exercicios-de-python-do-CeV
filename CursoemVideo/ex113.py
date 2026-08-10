"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

try:
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

    def leiafloat(msg):
        valido = False
        entrada = str(input(msg)).strip()
        cont = 0
        while not valido:
            cont = entrada.count(',') + entrada.count('.')
            if entrada.isalpha() or entrada == '' or cont == 0 or cont > 1 or entrada[0] == ',' or entrada[0] == '.' or entrada[-1] == ',' or entrada[-1] == '.':
                print('\033[31mERRO: digite um número decimal válido!\033[m')
                entrada = str(input(msg)).strip()
            else:
                valido = True
                return entrada

    n1 = leiaint('Digite um número inteiro: ')
    n2 = leiafloat('Digite um número decimal: ')
    print('-=' * 30)
    print(f'O número inteiro digitado foi {n1} e o decimal foi {n2}')

except KeyboardInterrupt:
    print('\n\033[31mO usuário preferiu não informar os dados!\033[m')

except Exception as erro:
    print(f'\n\033[31mProblema encontrado: {erro.__class__}\033[m')

finally:
    print('Muito obrigado, volte sempre!')
