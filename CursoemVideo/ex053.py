"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndormo, desconsiderando os espaços."""

frase  = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
inverso = frase[::-1]
if inverso == frase:
    print (f'O inverso de "{frase}" é "{inverso}"')
    print(f'A frase digitada É UM PALINDROMO')
else:
    print (f'O inverso de "{frase}" é "{inverso}"')
    print (f'A frase digitada NÃO é um palindromo')