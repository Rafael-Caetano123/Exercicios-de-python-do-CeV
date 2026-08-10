"""Crie um programa que o usuário digite uma expressão qualquer que use parênteses. Seu programa deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta."""

expressao = list()
pilha = list()
expressao.append(str(input('Digite uma expressão: ')))
for palavra in expressao:
    for letra in palavra:
        if ' ' in expressao:
            expressao.remove(' ')
        if letra == '(':
            pilha.append(letra)
        if letra == ')' and '(' not in pilha:
            print('Sua expressão esta incorreta!')
            exit()
        if letra == ')' and '(' in pilha:
            pilha.remove('(')
if len(pilha) == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta incorreta!')