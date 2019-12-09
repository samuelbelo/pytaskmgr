import os
import time
import psutil
import pygame
from funcoes_globais import mostra_titulo
from funcoes_globais import mostra_titulo_h2
from aba1 import conteudo_1
from aba3 import *
from aba4 import grafic
from cores import *
from dicionario import *

# from aba3 import mostra_titulo_aba3


os.environ['SDL_VIDEO_CENTERED'] = '1'                                  #inicializa a tela no centro display
titulo_abas = ['Arquivos', 'Processos', 'Rede 1', 'Rede 2']

pygame.init()                                                           #inicializa os códigos do pygame

largura_tela, altura_tela = 1200, 800                                    #define as dimenções da tela

area = pygame.Rect(0, 0, largura_tela, altura_tela)
tela = pygame.display.set_mode((largura_tela, altura_tela))             #exibe a tela com as dimensões especificadas
tela.fill(cinza)
clock = pygame.time.Clock()


# Para imprimir o texto com o tempo
def mostra_tempo(tempo, minuto):
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 50), 0)
    mostra_titulo_tela()
    desenha_abas()
    fonte = pygame.font.Font(None, 24)
    text = fonte.render('Tempo: ' + f'{minuto}' + 'm' + f'{tempo}' + 's', 1, preto)
    textpos = text.get_rect(centerx=1130, centery=25)
    tela.blit(text, textpos)


def mostra_titulo_tela():
    font = pygame.font.Font(None, 30)
    text = font.render('Projeto de Bloco', 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=25)
    tela.blit(text, textpos)


# def mostra_titulo(tela, texto, x, y):
#     font = pygame.font.Font(None, 26)
#     text = font.render(texto, 1, preto)
#     textpos = text.get_rect(centerx=x + 100, centery=y + 155)
#     textpos.left = x
#     tela.blit(text, textpos)


def desenha_abas():
    for i in range(4):
        x = i * 300
        a = pygame.draw.rect(tela, darkBlue, (x, 50, 300, 50), 0)
        pygame.draw.rect(tela, branco, (x, 50, 300, 50), 1)
        mostra_titulo_abas(i, x)
        lista.append(a)


def mostra_titulo_abas(i, x):
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[i], 1, branco)
    textpos = text.get_rect(centerx=x + 150, centery=75)
    tela.blit(text, textpos)


# def mostra_titulo_h2(tela, texto, x, y):
#     font = pygame.font.Font('OpenSans-Regular.ttf', 14)
#     text = font.render(texto, 1, preto)
#     textpos = text.get_rect(centerx=x + 100, centery=y+150)
#     textpos.left = x
#     tela.blit(text, textpos)


caminho_pasta = os.getcwd()
arquivo = os.listdir(caminho_pasta)
titulo_arquivo = ['Arquivo', 'Tamanho', 'Criado em', 'Última Modificação']


def conteudo_aba1():
    conteudo_1()


soma_rss = sum([i["RSS"] for i in lista_dicionarios])/1024/1024/1024
soma_vms = sum([i["VMS"] for i in lista_dicionarios])/1024/1024/1024
soma=0
total_rss = sum([i["RSS"] for i in lista_dicionarios])/1024/1024
total_vms = sum([i["VMS"] for i in lista_dicionarios])/1024/1024
soma_media = 0
titulo_conteudo_aba2 = ['Processo', 'Nome', 'Tamanho vms', 'Tamanho rss', '% vms', '% rss']


def conteudo_aba2():
    soma_indices = 1
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    mostra_titulo(tela, f'Total de Momória Utilizada VMS: {total_vms}', 50, -40)
    mostra_titulo(tela, f'Total de Momória Utilizada RSS: {total_rss}', 50, -50)
    mostra_titulo(tela, titulo_conteudo_aba2[0], 50, 40)
    mostra_titulo(tela, titulo_conteudo_aba2[1], 200, 40)
    mostra_titulo(tela, titulo_conteudo_aba2[2], 400, 40)
    mostra_titulo(tela, titulo_conteudo_aba2[3], 600, 40)
    mostra_titulo(tela, titulo_conteudo_aba2[4], 800, 40)
    mostra_titulo(tela, titulo_conteudo_aba2[5], 1000, 40)

    for p in psutil.process_iter():
        if p.status() == "running":
            vms = p.memory_info().vms/1024/1024
            rss = p.memory_info().rss/1024/1024
            mostra_titulo_h2(tela, f'{p.pid}', 50, 50 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{p.name()}', 200, 50 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(vms, 2)} MB', 400, 50 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round(rss, 2)} MB', 600, 50 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((vms/(soma_vms*1024)) * 100, 2)}%', 800, 50 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{round((rss/(soma_rss*1024)) * 100, 2)}%', 1000, 50 + soma_indices * 22)
            soma_indices += 1


print(round(total_rss/1024/1024))
print(round(total_vms/1024/1024))



'''                       0      1        2        3             4              5               6              7    '''
titulo_conteudo_aba3 = ['PID', 'End.', 'Tipo', 'Status', 'Endereço Local', 'Porta L.', 'Endereço Remoto', 'Porta R.']


def conteudo_aba3():
    soma_indices = 1
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    mostra_titulo(tela, titulo_conteudo_aba3[0], 50, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[1], 150, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[2], 200, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[3], 250, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[4], 350, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[5], 650, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[6], 750, -40)
    mostra_titulo(tela, titulo_conteudo_aba3[7], 1100, -40)
    l_pid = list(set(lista_pid))
    
    for i in range(len(l_pid)):
        p = psutil.Process(l_pid[i])
        conn = p.connections()
        mostra_titulo_h2(tela, f'{p.pid}', 50, -30 + soma_indices * 22)
        
        mostra_titulo_h2(tela, f'{obtem_nome_familia(conn[0].family)}', 150, -30 + soma_indices * 22)
        mostra_titulo_h2(tela, f'{obtem_tipo_socket(conn[0].type)}', 200, -30 + soma_indices * 22)
        mostra_titulo_h2(tela, f'{conn[0].status}', 250, -30 + soma_indices * 22)
        mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].laddr[0])}', 350, -30 + soma_indices * 22)
        mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].laddr[1])}', 650, -30 + soma_indices * 22)
        if obtem_dados_conexao_remota(conn[0].raddr) != '-':
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].raddr[0])}', 750, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].raddr[1])}', 1100, -30 + soma_indices * 22)
        else:
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].raddr)}', 750, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[0].raddr)}', 1100, -30 + soma_indices * 22)
        
        soma_indices += 1


def conteudo_aba4():
    mostra_titulo_h2(tela, "Gráfico de Processos PID x VMS", 500, -40)
    grafic(tela)
  

conta_clocks = 0
conta_segundos = 0
conta_minutos = 0
lista = []
controle_aba2 = False
controle_aba4 = False
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
                        conteudo_aba1()
                        controle_aba2 = False
                        break
                    elif q == lista[1]:
                        conteudo_aba2()
                        controle_aba2 = True
                        break
                    elif q == lista[2]:
                        controle_aba2 = False
                        conteudo_aba3()
                        break
                    elif q == lista[3]:
                        controle_aba2 = False
                        controle_aba4 = True
                        conteudo_aba4()
                        break

    if controle_aba2 is True:
        conteudo_aba2()

    if controle_aba4 is True:
        conteudo_aba4()

    if event.type == pygame.QUIT:                                   #se clicar no X fecha a tela
        terminou = True

    conta_clocks = conta_clocks + 1

    if conta_clocks == 50:
        conta_segundos += 1
        conta_clocks = 0

    if conta_segundos == 60:
        conta_segundos = 0
        conta_minutos += 1

    mostra_tempo(conta_segundos, conta_minutos)

    pygame.display.update()                                             # Atualiza o desenho na tela

    clock.tick(50)

pygame.display.quit()                                                   #fecha a tela exibida
pygame.quit()
