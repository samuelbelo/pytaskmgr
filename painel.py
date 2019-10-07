import pygame
import os
import pygame.freetype
from constants import (branco, preto, azul, azul_2, darkBlue, vermelho, verde, cinza, cinza_escuro,laranja, azul_pantone)

class Painel():
    def __init__(self):
        self.largura = 800
        self.altura = 710
        self.x = 0
        self.y = 90
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = branco
        # self.titulo = titulo_abas[0]

    def desenha_painel(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        # pygame.draw.rect(tela, cinza, self.area, 1)