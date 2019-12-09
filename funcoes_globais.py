import os
import pygame
from cores import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
largura_tela, altura_tela = 1200, 800
tela = pygame.display.set_mode((largura_tela, altura_tela))


def mostra_titulo_tela():
    font = pygame.font.Font(None, 30)
    text = font.render('Projeto de Bloco', 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_h2(tela, texto, x, y):
    font = pygame.font.Font('OpenSans-Regular.ttf', 14)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=x + 100, centery=y+150)
    textpos.left = x
    tela.blit(text, textpos)


def mostra_titulo(tela, texto, x, y):
    font = pygame.font.Font(None, 26)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=x + 100, centery=y + 155)
    textpos.left = x
    tela.blit(text, textpos)
