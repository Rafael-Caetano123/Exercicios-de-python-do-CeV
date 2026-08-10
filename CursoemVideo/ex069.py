"""Crie um programa que leia o nome e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos"""

maior_idade = cont_homens = menor_mulher = 0
while True:
    print('\033[1;36m-' * 30)
    print('     CADASTRE UMA PESSOA')
    print ('-' * 30,'\033[m')
    idade = int(input('Idade: '))
    if idade > 18:
        maior_idade += 1
    sexo = str(input('Sexo: [M/F] -> ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        print('-' * 30)
        print('\033[1;31mSexo inválido, tente novamente!\033[m')
        sexo = str(input('Sexo: [M/F] -> ')).upper().strip()
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        menor_mulher += 1
    print('-' * 30)
    alternativa = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    while alternativa != 'S' and alternativa != 'N':
        print('-' * 30)
        print('\033[1;31mResposta inválida, tente novamente!\033[m')
        alternativa = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    if alternativa == 'N':
        print('-' * 30)
        break
    print('-' * 30)
    print()
print()
print('\033[1;33m================ DADOS ==================\033[m')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Total de homens cadastrados: {cont_homens}')
print(f'Total de mulheres com menos de 20 anos: {menor_mulher}')