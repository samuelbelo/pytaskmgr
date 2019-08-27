import pygame
import random
import psutil

branco = (255,255,255)
preto = (0,0,0)

largura_tela, altura_tela = 800,600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Gerenciador de tarefas")
pygame.font.init()
terminou = False


pygame.font.init()
font = pygame.font.Font(None, 32)


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


while not terminou:
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()
    clock.tick(1)

pygame.display.quit()