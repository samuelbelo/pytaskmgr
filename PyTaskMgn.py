import pygame, random

branco = (255,255,255)
preto = (0,0,0)

pygame.font.init()
terminou = False

largura_tela, altura_tela = 800,600
tela = pygame.display.set_mode((largura_tela, altura_tela))

def mostra_titulo():
    font = pygame.font.Font(None, 24)
    text = font.render("51", 1, preto)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)
    
while not terminou:
    tela.fill(branco)
    mostra_titulo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()

pygame.display.quit()