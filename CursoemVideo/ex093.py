"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um diconário, incluindo o total de gols feitos durante o campeonato."""

dados = dict()
dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
tot_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? -> '))
gols = list()
for jogos in range(tot_partidas):
    gols.append(int(input(f'Quantos gols na {jogos+1}ª partida? -> ')))
dados['gols'] = gols[:]
dados['tot_gols'] = sum(gols)
print('=-' * 30)
print('======= DADOS DO JOGADOR =======')
print(f'Nome do jogador -> {dados["nome"]}')
print(f'Sequência de gols -> {dados["gols"]}')
print(f'Número total de gols -> {dados["tot_gols"]}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {tot_partidas} partidas.')
for i, gol in enumerate(gols):
    print(f'-> Na {i+1}ª partida fez {gol} gol(s)')
print(f'Foram um total de {dados["tot_gols"]} gols em {tot_partidas} partidas.')
