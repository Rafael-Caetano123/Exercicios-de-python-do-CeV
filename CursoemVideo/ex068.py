"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
print('\033[1;35m=-\033[m' * 16)
print('\33[1;38m     JOGO DO PAR OU IMPAR\033[m')
print('\033[1;35m=-\033[m' * 16)
total_vit = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    palpite = str(input('Par ou Ímpar? [P/I] -> ')).upper().strip()
    if palpite != 'P' and palpite != 'I':
        print('=-' * 20)
        print('\033[1;33mResposta inválida, tente novamente\033[m')
        print('=-' * 20)
        palpite = str(input('Par ou Ímpar? [P/I] -> ')).upper().strip()
    resultado = computador + jogador
    if palpite == 'P' and resultado % 2 == 0:
        print('=-' * 29)
        print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu PAR')
        print('=-' * 29)
        print('\033[1;32mVOCÊ VENCEU!!!\033[m')
        print('Vamor jogar novamente...')
        print('=' * 58)
        total_vit += 1
    elif palpite == 'I' and resultado % 2 != 0:
        print('=-' * 29)
        print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu ÍMPAR')
        print('=-' * 29)
        print('\033[1;32mVOCÊ VENCEU!!!\033[m')
        print('Vamos jogar novamente...')
        print('=' * 58)
        total_vit += 1
    else:
        print('=-' * 29)
        if palpite == 'P' and resultado % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu ÍMPAR')
        elif palpite == 'I' and resultado % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. No total de {resultado} deu PAR')
        print('=-' * 29)
        break
print('\033[1;31mVocê Perdeu!\033[m')
print('=' * 58)
if total_vit == 1:
    print('GAME OVER! Você venceu apenas 1 vez.')
elif total_vit > 1:
    print(f'GAME OVER! Você venceu {total_vit} vezes.')
else:
    print('GAME OVER! Você não venceu nenhuma vez.')