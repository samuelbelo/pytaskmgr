import pygame
import PyTaskMgn

pygame.init()

black = (0,0,0)
largura_tela, altura_tela = 800,600
tela = pygame.display.set_mode((largura_tela, altura_tela))

def cria_quadrado(tela):
    quadrados = pygame.draw.rect(tela, black, [75, 10, 50, 20], 2)
    return quadrados



pygame.quit()
    
    
