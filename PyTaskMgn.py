import pygame
import random
import psutil

branco = (255,255,255)
preto = (0,0,0)

pygame.font.init()
terminou = False

largura_tela, altura_tela = 800,600
tela = pygame.display.set_mode((largura_tela, altura_tela))


def mostra_titulo():
    font = pygame.font.Font(None, 24)
    text = font.render("Py Task Manager", 2, preto)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)


def mostra_memoria():
    mem = psutil.virtual_memory()
    capacidade = round(mem.total / (1024 * 1024 * 1024), 2)
    fonte_memo = pygame.font.Font(None, 24)
    """estou recebendo o erro: TypeError: integer argument expected, got float na linha abaixo"""
    text = fonte_memo.render("Memoria total: ", capacidade, 2, preto)
    textpos = fonteMemo.get_rect(centerx=tela.get_width() / 2)
    tela.blit(text,textpos)


while not terminou:
    tela.fill(branco)
    mostra_titulo()
    mostra_memoria()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()


pygame.display.quit()