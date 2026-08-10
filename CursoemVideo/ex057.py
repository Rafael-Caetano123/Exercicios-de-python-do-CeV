"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print()
        print('Sexo invalido, tente novamente:')
        print('           ↓')
    else:
        print(f'Sexo {sexo} registrado com sucesso!')