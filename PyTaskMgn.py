import pygame
import psutil
from aba import Aba
from constants import(branco, preto, azul, vermelho, largura_tela, altura_tela, dicionario)



tela = pygame.display.set_mode((largura_tela, altura_tela))
valores_Bytes = dicionario.values()
soma = sum(dicionario.values())
soma = soma/1024/1024
#soma_media = soma/len(dicionario)

pygame.display.set_caption("Gerenciador de tarefas")
terminou = False


pygame.font.init()
font = pygame.font.Font(None, 32)


def cria_abas():
    lista_abas = []
    for i in range(0,4):
        aba_type = 1
        aba = Aba(i, preto)
        aba.desenha(tela)
        lista_abas.append(aba)
        mostra_titulo(f"ABA[i]", (largura_tela/4 * aba_type)+100)
    return lista_abas

def mostra_titulo(texto, y, fonte=20):
    font = pygame.font.Font(None, fonte)
    text = font.render(texto, 1, preto)
    textpos = text.get.rect(center=(tela.get_width()/2,y))
    textpos.left = 100
    tela.blit(text, textpos)
    
def mostra_titulo_aba(texto, x):
    font = pygame.font.Font(None, 24)
    text = font.render*(texto, 1, branco)
    textpos = text.get_rect(center=(x, 30))
    tela.blit(text, textpos)

#def formata_valores:
    
    
def cria_abas():
    lista_de_abas = []
    for i in range(0,4):
        aba_type = i
        aba = Aba(i, preto)
        aba.desenha(tela)
        lista_de_abas.append(aba)
        mostra_titulo(f"aba {i}", (largura_tela/4 * aba_type) + 100)


tela.fill(branco)
aba0, aba1, aba2, aba3 = cria_abas()

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.fill(branco)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


cont = 60
clock = pygame.time.Clock()
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if cont == 60:
            mostra_uso_memoria()
            cont = 0
    pygame.display.update()
    clock.tick(60)
    cont = cont + 1

pygame.display.quit()
