import pygame
import psutil
import time
import os
from cores import *
from teste import *

os.environ['SDL_VIDEO_CENTERED'] = '1'                                  #inicializa a tela no centro display
titulo_abas = ['Arquivos', 'Processos', 'Rede 1', 'Rede 2']

pygame.init()                                                           #inicializa os códigos do pygame

largura_tela, altura_tela = 800, 800                                    #define as dimenções da tela

area = pygame.Rect(0, 0, largura_tela, altura_tela)
tela = pygame.display.set_mode((largura_tela, altura_tela))             #exibe a tela com as dimensões especificadas
tela.fill(cinza)
clock = pygame.time.Clock()


# Para imprimir o texto com o tempo
def mostra_tempo(tempo, minuto):
    pygame.draw.rect(tela, cinza, (0, 0, 800, 50), 0)
    mostra_titulo_tela()
    fonte = pygame.font.Font(None, 24)
    text = fonte.render('Tempo: ' + f'{minuto}' + 'm' + f'{tempo}' + 's', 1, preto)
    textpos = text.get_rect(centerx=730, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_tela():
    font = pygame.font.Font(None, 30)
    text = font.render('Projeto de Bloco', 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_teste():
    pygame.draw.rect(tela, laranja, (0, 100, 800, 700))  # exibe a tela com as dimensões especificadas
    font = pygame.font.Font(None, 30)
    text = font.render('Teste!!!!', 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=tela.get_width() / 2)
    tela.blit(text, textpos)


def desenha_abas():
    for i in range(4):
        eixo_x = i * 200
        pygame.draw.rect(tela, darkBlue, (eixo_x, 50, 200, 50), 0)
        a = pygame.draw.rect(tela, darkBlue, (eixo_x, 50, 200, 50), 0)
        pygame.draw.rect(tela, branco, (eixo_x, 50, 200, 50), 1)
        mostra_titulo_abas(i, eixo_x)
        lista.append(a)


def mostra_titulo_abas(i, eixo_x):
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[i], 1, branco)
    textpos = text.get_rect(centerx=eixo_x + 100, centery=75)
    tela.blit(text, textpos)


def mostra_titulo_h2(tela, texto, x, y):
    font = pygame.font.Font(None, 20)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=50, centery=150)
    textpos.left = 50
    tela.blit(text, textpos)


def desenha_tela_inicial():
    desenha_abas()
    
    


soma_rss = sum([i["RSS"] for i in lista_dicionarios])/1024/1024/1024
soma_vms = sum([i["VMS"] for i in lista_dicionarios])/1024/1024/1024
soma = 0
soma_media = 0

def formata_valores():
    soma_indices = 1
    for p in psutil.process_iter():
        if p.status() == "running":
            vms = p.memory_info().vms/1024/1024
            rss = p.memory_info().rss/1024/1024
            mostra_titulo_h2(tela, f'{p.pid}', 100, 160 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{p.name()}', 160, 160 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(vms, 2)}MB', 400, 160 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(rss, 2)}MB', 500, 160 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((vms/(soma_vms*1024)) * 100, 2)}%', 620, 160 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((rss/(soma_rss*1024)) * 100, 2)}%', 700, 160 + soma_indices * 22)
            soma_indices = soma_indices + 1        




conta_clocks = 0
conta_segundos = 0
conta_minutos = 0
lista = []

terminou = False                                                        #variável para manter a tela aberta
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for q in lista:
                if q.collidepoint(pos):
                    if q == lista[0]:
                        tela.fill(cinza)
                        break
                    elif q == lista[1]:
                        mostra_titulo_h2(f'{formata_valores()}', 150)
                        print(lista_dicionarios)
                        #tela.fill(cinza_escuro)
                        break
                    elif q == lista[2]:
                        mostra_titulo_teste()
                        break
                    elif q == lista[3]:
                        tela.fill(branco)
                        break

        if event.type == pygame.QUIT:                                   #se clicar no X fecha a tela
            terminou = True

    conta_clocks = conta_clocks + 1

    if conta_clocks == 50:
        conta_segundos += 1
        conta_clocks = 0

    # desenha_tela_inicial()
    desenha_abas()

    # Mostra o tempo atualizado
    if conta_segundos == 60:
        conta_segundos = 0
        conta_minutos += 1

    mostra_tempo(conta_segundos, conta_minutos)

    pygame.display.update()                                             # Atualiza o desenho na tela

    clock.tick(50)

pygame.display.quit()                                                   #fecha a tela exibida
pygame.quit()
