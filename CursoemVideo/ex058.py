"""melhore o DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
print('\033[1;36m=-\033[m' * 20)
print('\033[1;33m     Jogo da Adivinhação v.2.0\033[m')
print('\033[1;36m=-\033[m' * 20)
print ('''\033[1;32mOi sou seu computador pensei em um número de 1 a 10
Tente adivinhar qual é\033[m''')
computador = randint(0, 10)
jogador = int(input('Qual seu palpite? '))
tentativas = 1
while jogador != computador:
    if jogador > computador:
        print ('Menor...Tente novamente')
        jogador = int(input('Qual seu palpite? '))
        tentativas += 1
    elif jogador < computador:
        print ('Maior...Tente novamente')
        jogador = int(input('Qual seu palpite? '))
        tentativas += 1
print ('Parabéns você acertou!!!')
print (f'Você acertou com {tentativas} tentativas')