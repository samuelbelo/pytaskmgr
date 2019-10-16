import pygame
import os
from cores import *

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
        x = i * 200
        pygame.draw.rect(tela, darkBlue, (x, 50, 200, 50), 0)
        a = pygame.draw.rect(tela, darkBlue, (x, 50, 200, 50), 0)
        pygame.draw.rect(tela, branco, (x, 50, 200, 50), 1)
        mostra_titulo_abas(i, x)
        lista.append(a)


def mostra_titulo_abas(i, x):
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[i], 1, branco)
    textpos = text.get_rect(centerx=x + 100, centery=75)
    tela.blit(text, textpos)


def mostra_titulo_h2(texto, y):
    font = pygame.font.Font(None, 20)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=50, centery=150)
    textpos.left = 50
    tela.blit(text, textpos)


def desenha_tela_inicial():
    desenha_abas()


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
                        mostra_titulo_teste()
                        break
                    elif q == lista[1]:
                        tela.fill(cinza_escuro)
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
