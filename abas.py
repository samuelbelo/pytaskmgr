import pygame
import subprocess
import psutil
#import pid
import time
import os
import pygame.freetype
from constants import (branco, preto, azul, azul_2, darkBlue, vermelho, verde, cinza, cinza_escuro,laranja, azul_pantone)
from painel import Painel

titulo_abas = ['Arquivos', 'Processos', 'Rede 1', 'Rede 2']

class Abas():
    def __init__(self):
        titulo_abas = ['Arquivos', 'Processos', 'Rede 1', 'Rede 2']
        self.largura = 200
        self.altura = 50
        self.x = 0
        self.y = 40
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = azul_pantone
        self.titulo = titulo_abas[0]

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        pygame.draw.rect(tela, branco, self.area, 1)
