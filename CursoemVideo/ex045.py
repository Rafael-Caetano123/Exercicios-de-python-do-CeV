"""Crie um programa que faça o computador jogar Jokênpo com você"""

from random import choice
from time import sleep
print ('\033[1;36m======= VAMOS JOGAR JOKÊNPO! =======\033[m')
print ('\033[1;33m-\033[m' * 40)
print ('[ 1 ] PEDRA')
print ('[ 2 ] PAPEL')
print ('[ 3 ] TESOURA')
opção = int(input('Escolha uma das opções: '))
print ('\033[1;33m-\033[m' * 40)
opções = ('PEDRA', 'PAPEL', 'TESOURA')
pc = choice(opções)
print ('\033[1;36mJO\033[m'), sleep (1)
print ('\033[1;36mKÊN\033[m'),sleep (1)
print ('\033[1;36mPO\033[m')
if opção == 1 and pc == 'TESOURA':
    print('-=' * 13)
    print(f'Jogador jogou PEDRA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;32mVocê ganhou!!!\033[m')
elif opção == 2 and pc == 'PEDRA':
    print('-=' * 13)
    print(f'Jogador jogou PAPEL')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;32mVocê ganhou!!!\033[m')
elif opção == 3 and pc == 'PAPEL':
    print('-=' * 13)
    print(f'Jogador jogou TESOURA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;32mVocê ganhou!!!\033[m')
elif opção == 1 and pc == 'PAPEL':
    print('-=' * 13)
    print(f'Jogador jogou PEDRA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;31mVocê perdeu!\033[m')
elif opção == 2 and pc == 'TESOURA':
    print('-=' * 13)
    print(f'Jogador jogou PAPEL')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;31mVocê perdeu!\033[m')
elif opção == 3 and pc == 'PEDRA':
    print('-=' * 13)
    print(f'Jogador jogou TESOURA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;31mVocê perdeu!\033[m')
elif opção == 1 and pc == 'PEDRA':
    print('-=' * 13)
    print(f'Jogador jogou PEDRA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;33mEMPATE!\033[m')
elif opção == 2 and pc == 'PAPEL':
    print('-=' * 13)
    print(f'Jogador jogou PAPEL')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;33mEMPATE!\033[m')
elif opção == 3 and pc == 'TESOURA':
    print('-=' * 13)
    print(f'Jogador jogou TESOURA')
    print(f'Computador jogou {pc}')
    print('=-' * 13)
    print ('\033[1;33mEMPATE!\033[m')
elif opção != 1 or 2 or 3:
    print ('\033[1;31mOpção inválida!')