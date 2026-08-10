"""Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usúario tentar
descobrir qual foi número escolhido pelo comptutador.
o programa deverá mostrar na tela se o usúario venceu ou perdeu."""

from random import randint
from time import sleep
print ('-' * 50)
print ('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print ('-' * 50)
computador = randint(0,5)
jogador = int(input('Escolha um número de 0 a 5: '))
print ('PROCESSANDO...'),sleep(2)
if computador == jogador:
    print ('PARABÉNS! Você conseguiu me vencer!')
else:
    print (f'GANHEI! eu pensei no número {computador} não no {jogador}')