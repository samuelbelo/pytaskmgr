# coding=utf-8
import psutil
import pygame

branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

largura_tela, altura_tela = 800,600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Gerenciador de tarefas")
terminou = False

pygame.font.init()
font = pygame.font.Font(None, 32)

def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * capacidade/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    tela.blit(text, (20, 10))

cont = 60
clock = pygame.time.Clock()
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if cont == 60:
            mostra_uso_cpu()
            cont = 0
    pygame.display.update()
    clock.tick(60)
    cont = cont + 1

pygame.display.quit()