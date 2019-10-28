import pygame
import os
import time
# import psutil
from dicionario import *
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
    desenha_abas()
    fonte = pygame.font.Font(None, 24)
    text = fonte.render('Tempo: ' + f'{minuto}' + 'm' + f'{tempo}' + 's', 1, preto)
    textpos = text.get_rect(centerx=730, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_tela():
    font = pygame.font.Font(None, 30)
    text = font.render('Projeto de Bloco', 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_teste(texto):
    pygame.draw.rect(tela, laranja, (0, 100, 800, 700))  # exibe a tela com as dimensões especificadas
    font = pygame.font.Font(None, 30)
    text = font.render(texto, 1, preto)
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


def mostra_titulo_h2(tela, texto, x, y):
    font = pygame.font.Font('OpenSans-Regular.ttf', 15)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=x + 100, centery=y+150)
    textpos.left = x
    tela.blit(text, textpos)


caminho_pasta = os.getcwd()
arquivo = os.listdir(caminho_pasta)
titulo_arquivo = ['Arquivo', 'Tamanho', 'Criado em', 'Última Modificação']


def conteudo_aba0():
    soma = 1
    pygame.draw.rect(tela, cinza, (0, 0, 800, 800), 0)
    mostra_titulo_h2(tela, f'{titulo_arquivo[0]}', x=25, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[1]}', x=200, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[2]}', x=400, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[3]}', x=600, y=5)

    for i in range(len(arquivo)):
        status_arquivo = os.stat(f'{arquivo[i]}')
        # data_criacao = time.localtime(status_arquivo.st_ctime)
        # ultima_modificacao = time.localtime(status_arquivo.st_mtime)
        mostra_titulo_h2(tela, f'{arquivo[i]}', x=25, y=soma * 30)
        mostra_titulo_h2(tela, f'{status_arquivo.st_size/1024:.2f} KBytes', x=200, y=soma*30)
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_ctime))}', x=400, y=soma * 30)
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_mtime))}', x=600, y=soma * 30)
        soma += 1
        os.times()


soma_rss = sum([i["RSS"] for i in lista_dicionarios])/1024/1024/1024
soma_vms = sum([i["VMS"] for i in lista_dicionarios])/1024/1024/1024
soma = 0
soma_media = 0
titulo_conteudo_aba1 = ['Processo', 'Nome', 'Tamanho vms', 'Tamanho rss', '% vms', '% rss']


def conteudo_aba1():
    soma_indices = 1
    # mostra_tempo(tempo, minuto)
    pygame.draw.rect(tela, cinza, (0, 0, 800, 800), 0)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[0], 50, -40)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[1], 150, -40)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[2], 320, -40)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[3], 470, -40)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[4], 600, -40)
    mostra_titulo_h2(tela, titulo_conteudo_aba1[5], 700, -40)

    for p in psutil.process_iter():
        if p.status() == "running":

            vms = p.memory_info().vms/1024/1024
            rss = p.memory_info().rss/1024/1024
            mostra_titulo_h2(tela, f'{p.pid}', 50, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{p.name()}', 150, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(vms, 2)} MB', 320, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(rss, 2)} MB', 470, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((vms/(soma_vms*1024)) * 100, 2)}%', 600, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((rss/(soma_rss*1024)) * 100, 2)}%', 700, -30 + soma_indices * 22)
            soma_indices += 1


conta_clocks = 0
conta_segundos = 0
conta_minutos = 0
lista = []
aba1 = False

terminou = False
#variável para manter a tela aberta
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for q in lista:
                if q.collidepoint(pos):
                    if q == lista[0]:
                        conteudo_aba0()
                        aba1 = False
                        break
                    elif q == lista[1]:
                        conteudo_aba1()
                        aba1 = True
                        break
                    elif q == lista[2]:
                        aba1 = False
                        mostra_titulo_teste('Vai que cola?!')
                        break
                    elif q == lista[3]:
                        aba1 = False
                        tela.fill(branco)
                        break

    if aba1 is True:
        conteudo_aba1()

    if event.type == pygame.QUIT:                                   #se clicar no X fecha a tela
        terminou = True

    conta_clocks = conta_clocks + 1

    # conteudo_aba1()

    if conta_clocks == 50:
        conta_segundos += 1
        conta_clocks = 0

    # desenha_tela_inicial()
    # desenha_abas()

    # Mostra o tempo atualizado
    if conta_segundos == 60:
        conta_segundos = 0
        conta_minutos += 1

    mostra_tempo(conta_segundos, conta_minutos)

    pygame.display.update()                                             # Atualiza o desenho na tela

    clock.tick(50)

pygame.display.quit()                                                   #fecha a tela exibida
pygame.quit()
