# coding=utf-8

import pygame
import os
import pygame.freetype
from constants import (branco, preto, azul, azul_2, darkBlue, vermelho, verde, cinza, cinza_escuro,laranja)



titulo_abas = ['Arquivos', 'Processos', 'Rede 1', 'Rede 2']

# Inicialização da fonte
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.font.init()
terminou = False


# Dimensões da tela
largura_tela, altura_tela = 800, 800
abas_iniciais = 4
tela = pygame.display.set_mode((largura_tela, altura_tela))

# dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
#               'antonio': 123456456, 'carlos': 91257581,
#               'cesar': 987458, 'rosemary': 789456125}
dicionario =  [{'rss': 113979392, 'vms': 114520064, 'pid': 88, 'nome': 'Registry', 'percento': 379.85},
              {'rss': 35794944, 'vms': 20525056, 'pid': 948, 'nome': 'chrome.exe', 'percento': 50.7},
              {'rss': 34332672, 'vms': 17887232, 'pid': 984, 'nome': 'svchost.exe', 'percento': 44.54},
              {'rss': 255979520, 'vms': 22016000, 'pid': 1012, 'nome': 'fontdrvhost.exe', 'percento': 977.67},
              {'rss': 35188736, 'vms': 25378816, 'pid': 1708, 'nome': 'svchost.exe', 'percento': 48.14},
              {'rss': 25681920, 'vms': 7020544, 'pid': 2300, 'nome': 'ApplicationFrameHost.exe', 'percento': 8.12},
              {'rss': 64212992, 'vms': 30863360, 'pid': 2372, 'nome': 'MicrosoftEdge.exe', 'percento': 170.34},
              {'rss': 26263552, 'vms': 6246400, 'pid': 2448, 'nome': 'MicrosoftEdgeCP.exe', 'percento': 10.57},
              {'rss': 114982912, 'vms': 154681344, 'pid': 2628, 'nome': 'MsMpEng.exe', 'percento': 384.08},
              {'rss': 25030656, 'vms': 9220096, 'pid': 4024, 'nome': 'svchost.exe', 'percento': 5.38},
              {'rss': 37093376, 'vms': 20942848, 'pid': 4116, 'nome': 'SkypeApp.exe', 'percento': 56.16},
              {'rss': 56758272, 'vms': 42430464, 'pid': 4760, 'nome': 'svchost.exe', 'percento': 138.95},
              {'rss': 45293568, 'vms': 24764416, 'pid': 5328, 'nome': 'vmware-hostd.exe', 'percento': 90.69},
              {'rss': 124157952, 'vms': 55316480, 'pid': 5400, 'nome': 'explorer.exe', 'percento': 422.7},
              {'rss': 24948736, 'vms': 5890048, 'pid': 5432, 'nome': 'sihost.exe', 'percento': 5.03},
              {'rss': 34627584, 'vms': 8003584, 'pid': 6560, 'nome': 'svchost.exe', 'percento': 45.78},
              {'rss': 79331328, 'vms': 33001472, 'pid': 6644, 'nome': 'ShellExperienceHost.exe', 'percento': 233.98},
              {'rss': 118439936, 'vms': 61276160, 'pid': 7024, 'nome': 'SearchUI.exe', 'percento': 398.63},
              {'rss': 80060416, 'vms': 55767040, 'pid': 7052, 'nome': 'chrome.exe', 'percento': 237.05},
              {'rss': 170975232, 'vms': 144072704, 'pid': 7468, 'nome': 'chrome.exe', 'percento': 619.8},
              {'rss': 78249984, 'vms': 47955968, 'pid': 7520, 'nome': 'thonny.exe', 'percento': 229.43},
              {'rss': 36786176, 'vms': 21307392, 'pid': 7628, 'nome': 'chrome.exe', 'percento': 54.87},
              {'rss': 102436864, 'vms': 77463552, 'pid': 7776, 'nome': 'chrome.exe', 'percento': 331.26},
              {'rss': 70623232, 'vms': 133386240, 'pid': 7868, 'nome': 'chrome.exe', 'percento': 197.32},
              {'rss': 125968384, 'vms': 63152128, 'pid': 7900, 'nome': 'chrome.exe', 'percento': 430.32},
              {'rss': 47972352, 'vms': 31125504, 'pid': 8384, 'nome': 'Microsoft.Photos.exe', 'percento': 101.96},
              {'rss': 48463872, 'vms': 38649856, 'pid': 9120, 'nome': 'dwm.exe', 'percento': 104.03},
              {'rss': 192319488, 'vms': 167886848, 'pid': 9220, 'nome': 'chrome.exe', 'percento': 709.66},
              {'rss': 67276800, 'vms': 41480192, 'pid': 9784, 'nome': 'chrome.exe', 'percento': 183.23},
              {'rss': 60825600, 'vms': 35332096, 'pid': 9972, 'nome': 'chrome.exe', 'percento': 156.07}]


# Soma e Cálcula as Médias das chaves dos dicionários em MB
for i in range(len(dicionario)):
    teste = [dicionario[i].setdefault('rss'), dicionario[i].setdefault('vms'), dicionario[i].setdefault('pid'),
      dicionario[i].setdefault('percento')]
    soma_rss, soma_vms = teste[0], teste[1]
    soma_rss, soma_vms = soma_rss / 1024 / 1024, soma_vms / 1024 / 1024
    soma_media_rss, soma_media_vss = soma_rss / len(dicionario), soma_vms / len(dicionario)

# valores_Bytes = dicionario.values()
# soma = sum(dicionario.values())
# soma = soma / 1024 / 1024
# soma_media = soma / len(dicionario)

class Abas():
    def __init__(self):
        self.largura = 200
        self.altura = 50
        self.x = 0
        self.y = 40
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = verde
        self.titulo = titulo_abas[0]

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        pygame.draw.rect(tela, cinza, self.area, 1)


class Painel():
    def __init__(self):
        self.largura = 800
        self.altura = 710
        self.x = 0
        self.y = 90
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = cinza_escuro
        # self.titulo = titulo_abas[0]

    def desenha_painel(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        # pygame.draw.rect(tela, cinza, self.area, 1)


# Converte os valores das chaves do dicionário em MB
for i in range(len(dicionario)):
    valor = dicionario[i].get('rss')
    converter_mb = valor / 1024 / 1024
    dicionario[i] = round(converter_mb, 2)


def mostra_titulo():
    font = pygame.font.Font(None, 24)
    text = font.render("Gerenciador de Tarefas", 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=20)
    tela.blit(text, textpos)


def mostra_aba_1():
    q = Abas()
    q.area = pygame.Rect(q.x, q.y, q.largura, q.altura)
    return q.area


def mostra_aba_2():
    q = Abas()
    q.area = pygame.Rect(q.x + 200, q.y, q.largura, q.altura)
    return q.area


def conteudo_aba_2():
    soma_indices = 1
    # Obtém lista de arquivos e diretórios do diretório corrente:
    lista = os.listdir()
    dic = {} # cria dicionário
    for i in lista: # Varia na lista dos arquivos e diretórios
        if os.path.isfile(i): # checa se é um arquivo
            # Cria uma lista para cada arquivo. Esta lista contém o
            # tamanho, data de criação e data de modificação.
            dic[i] = []
            dic[i].append(os.stat(i).st_size) # Tamanho
            dic[i].append(os.stat(i).st_atime) # Tempo de criação
            dic[i].append(os.stat(i).st_mtime) # Tempo de modificação

            mostra_titulo_h2(f"{os.stat(i).st_size}", 150 + soma_indices * 15)
            soma_indices = soma_indices + 1
        

def mostra_aba_3():
    q = Abas()
    q.area = pygame.Rect(q.x + 400, q.y, q.largura, q.altura)
    return q.area


def mostra_aba_4():
    q = Abas()
    q.area = pygame.Rect(q.x + 600, q.y, q.largura, q.altura)
    return q.area


def mostra_painel(tela):
    p = Painel()
    p.desenha_painel(tela)


def mostra_titulo_h2(texto, y):
    font = pygame.font.Font(None, 20)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(center=(tela.get_width() / 2, y + 40))
    textpos.left = 250
    tela.blit(text, textpos)


def formata_valores(dicionario, soma):
    soma_indices = 1
    for i in range(len(dicionario)):
        dicionario[i] = round(dicionario[i], 0)
        porcentagem = round((dicionario[i] / soma_rss) * 100, 2)
        p = (f'{soma_indices:^10} {i:^20} {dicionario[i]:^30.2f} {porcentagem:^40.2f}')
        mostra_titulo_h2(p, 150 + soma_indices * 15)
        soma_indices = soma_indices + 1


pontos = 'Não'
indice_lista = 1


def mostra_click_botao():
    p = Painel()
    p.desenha_painel(tela)
    font = pygame.font.Font(None, 36)
    text = font.render(f'Clicou na Aba {indice_lista}? {pontos}', 1, branco)
    textpos = text.get_rect(center=(tela.get_width() / 2, tela.get_height() / 2))
    tela.blit(text, textpos)


tela.fill(cinza)
mostra_titulo()

lista_areas_abas = []
areas_abas = [mostra_aba_1(), mostra_aba_2(), mostra_aba_3(), mostra_aba_4()]


def inicia_aba():
    for i in range(0, abas_iniciais):
        q = Abas()
        q.area = areas_abas[i]
        q.titulo = titulo_abas[i]
        q.desenha(tela)

        q.x = i * 200 + 100
        q.y = 65

        lista_areas_abas.append(q)
        font = pygame.font.Font(None, 24)
        text = font.render(titulo_abas[i], 1, branco)
        textpos = text.get_rect(center=(q.x, q.y))
        tela.blit(text, textpos)


def mostra_tempo(tempo):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s", 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2)
    tela.blit(text, textpos)

# Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

# Variavel para contar quantos segundos se passaram
conta_segundos = 0
inicia_aba()
mostra_tempo(conta_segundos)
#criando o relogio
clock = pygame.time.Clock()

while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtém as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()

            # Checa se clicou em algum dos quadrados
            for q in lista_areas_abas:
                if q.area.collidepoint(pos):
                    if q == lista_areas_abas[1]:
                        pontos = 'Sim'
                        indice_lista = 2
                        mostra_painel(tela)
                        mostra_titulo_h2("ACME Inc. Uso do espaço em disco pelos usuários", 100)
                        mostra_titulo_h2("Nr.            Usuário            Espaço Utilizado            % do uso", 130)
                        formata_valores(dicionario, soma_rss)
                        # formata_valores()
                        mostra_titulo_h2(f"Total de memoria usada: {round(soma_rss, 2)} Mb", 650)
                        mostra_titulo_h2(f"Media de memoria usada: {round(soma_media_rss, 2)} Mb", 700)

                    elif q == lista_areas_abas[0]:
                        pontos = 'Sim'
                        mostra_painel(tela)
                        mostra_titulo_h2('Tamanho       Data de Modificação       Data de Criação       Nome', 100)
                        indice_lista = 1
                        conteudo_aba_2()
                        #mostra_click_botao()

                    elif q == lista_areas_abas[2]:
                        pontos = 'Sim'
                        indice_lista = 3
                        mostra_click_botao()

                    else:
                        pontos = 'Sim'
                        indice_lista = 4
                        mostra_click_botao()

        conta_clocks = conta_clocks + 1

        # A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
        if conta_clocks == 50:
            conta_segundos = conta_segundos + 1
            conta_clocks = 0

        if event.type == pygame.QUIT:
            terminou = True

    # Mostra o tempo atualizado
    mostra_tempo(conta_segundos)

    # Atualiza o desenho na tela
    pygame.display.update()
# Finaliza a janela do jogo
pygame.display.quit()
