"""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""

from time import sleep
elenco = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['tot_partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? -> '))
    for gol in range(jogador['tot_partidas']):
        gols.append(int(input(f'Quantos gols na {gol+1}ª partida? -> ')))
    jogador['gols'] = gols[:]
    jogador['tot_gols'] = sum(gols)
    elenco.append(jogador.copy())
    jogador.clear()
    gols.clear()
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida, tente novamente!')
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()
    print('-=' * 30)
    if resp == 'N':
        break
print(f'{"Nº":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
for i, j in enumerate(elenco):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["tot_gols"]:<5}')
print('-=' * 30)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe) -> Nº'))
    if opc == 999:
        break
    while opc > len(elenco) - 1:
        print('Erro, não contém nenhum jogador com este número!')
        opc = int(input('Mostrar dados de qual jogador? (999 interrompe) -> Nº'))
        print('-=' * 30)
        if opc == 999:
            break
    print('-=' * 30)
    print(f'===== Dados do jogador {elenco[opc]["nome"]} =====')
    for i, g in enumerate(elenco[opc]["gols"]):
        print(f'-> Na {i+1}ª partida fez {g} gol(s)')
        sleep(1)
    sleep(1)
    print(f'Foram um total de {elenco[opc]["tot_gols"]} gol(s) em {elenco[opc]["tot_partidas"]} partida(s)')
    print('-=' * 30)
print('-=' * 30)
print('Encerrando programa...')
sleep(3)
print('Programa encerrado, volte sempre!')