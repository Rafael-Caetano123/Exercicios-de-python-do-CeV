"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
a média de idade do grupo.
qual é o nome do homem mais velho.
quantas mulheres tem menos de 20 anos."""

media = 0
maior_nome_homem = ''
maior_idade_homem = 0
maior_idade_mulher = 0
menor_idade_mulher = 0
for dados in range(1, 5):
    print('\033[1;36m=-\033[m' * 5, f'\033[1;36m{dados}ª pessoa\033[m', '\033[1;36m=-\033[m' * 5)
    nome = str(input(f'Digite o nome da {dados}ª pessoa: ')).capitalize().strip()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Digite o sexo de {nome}: ')).upper().strip()
    media += idade / 4

    if sexo != 'FEMININO' and sexo != 'MASCULINO':
        print ('\033[1;31mSexo Incorrespondente, tente novemente!\033[m')
        exit()

    if sexo == 'MASCULINO' and idade > maior_idade_homem:
        maior_nome_homem = nome
        maior_idade_homem = idade

    if sexo == 'FEMININO' and idade > 20:
        maior_idade_mulher += 1

    if sexo == 'FEMININO' and idade <= 20:
        menor_idade_mulher += 1

print('\033[1;36m=-\033[m' * 15)
print()
print(f'A média de idade do grupo é de {media:.0f} anos')
print('-' * 60)

if maior_idade_homem > 0:
    print (f'O homem mais velho do grupo é o {maior_nome_homem} e ele tem {maior_idade_homem} anos')
    print('-' * 60)

if maior_idade_mulher > 0 and menor_idade_mulher > 0:
    print (f'Ao todo no grupo há {maior_idade_mulher} mulher(es) com mais de 20 anos')
    print (f'E {menor_idade_mulher} mulher(es) com menos de 20 anos')

elif maior_idade_mulher > 1:
    print (f'No grupo tem {maior_idade_mulher} mulher(es) com mais de 20 anos')

elif maior_idade_mulher == 0 and menor_idade_mulher > 1:
    print (f'No grupo ao todo há {menor_idade_mulher} mulher(es) com menos de 20 anos')