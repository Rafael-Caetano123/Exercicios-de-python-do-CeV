"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média."""

dados = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo [M/F] -> ')).strip().upper()
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('Sexo inválido, tente novamente!')
        pessoa['sexo'] = str(input('Sexo [M/F] -> ')).strip().upper()
    dados.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida, tente novamente!')
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    if resp == 'N':
        break
idades = list()
mulheres = list()
for p in dados:
    idades.append(p['idade'])
    if p["sexo"] == 'F':
        mulheres.append(p["nome"])
media = sum(idades) / len(idades)
acima_media = list()
for p in dados:
    if p['idade'] > media:
        acima_media.append(p)
print('-=' * 30)
print('======= DADOS DO GRUPO =======')
if len(dados) > 1:
    print(f'- Ao todo o grupo tem {len(dados)} pessoas')
else:
    print(f'- Apenas uma pessoa foi cadastrada')
print(f'- A média de idade do grupo é de {media:.0f} anos')
if len(mulheres) > 1:
    print(f'- As mulheres cadastradas foram: {mulheres}')
elif len(mulheres) == 1:
    print(f'- A única mulher cadastrada foi a {mulheres[0]}')
else:
    print('- Nenhuma mulher foi cadastrada')
if len(acima_media) == 0:
    print(f'- Nenhuma pessoa está com a idade acima da média de idade do grupo')
else:
    print('-=' * 30)
    print('- Lista de pessoas que estão com a média de idade acima:')
    for p in acima_media:
        print(f'  {p}')
