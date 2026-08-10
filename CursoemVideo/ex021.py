"""Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3"""

import pygame
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
sleep(30)

"""O programa funcionou mas eu apaguei o 'ex021.mp3' que faz o audio funcionar, por conta da memória que estava gastando"""