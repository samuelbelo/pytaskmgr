import pygame
# from main import *
from cores import *


def desenha_abas():
    for i in range(4):
        pygame.draw.rect(tela, darkBlue, (i * 200, 50, 200, 50), 0)
        pygame.draw.rect(tela, branco, (i * 200, 50, 200, 50), 1)
