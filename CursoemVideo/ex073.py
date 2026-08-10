"""Crie uma tupla com os 20 primeiros colocados da tabela do Brasileirão, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição está colocado o time que o usúario digitar"""

from time import sleep
times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia',
         'Fluminense', 'Botafogo', 'Vasco', 'São Paulo', 'Corinthians',
         'Grêmio', 'Bragantino', 'Atlético-Mg', 'Ceára', 'Internacional',
         'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')
print ('=-' * 135)
print (f'Lista de times Brasileirão (2025) -> {times}')
print ('=-' * 135)
sleep(2)
print (f'Os 5 primeiros times são -> {times[:5]}')
print ('=-' * 135)
sleep(2)
print (f'Os 4 últimos são -> {times[-4:]}')
print ('=-' * 135)
sleep(2)
print (f'Lista em ordem alfabética -> {sorted(times)}')
print ('=-' * 135)
while True:
    opcao = str(input('Você quer saber a posição de qual time? ')).strip().capitalize()
    while opcao not in times:
        print('Resposta inválida, tente novamente')
        opcao = str(input('Você quer saber a posição de qual time? ')).strip().capitalize()
    print (f'O time {opcao} está {times.index(opcao)+1}ª colocação.')
    resp = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    while resp != 'S' and resp != 'N':
        print('Resposta inválida, tente novamente')
        resp = str(input('Quer continuar? [S/N] -> ')).upper().strip()
    if resp == 'N':
        break
print('\033[1;32mPrograma encerrado com sucesso!')