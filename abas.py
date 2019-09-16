import psutil
import pygame
from constants import (branco, preto, azul, azul_2, darkBlue, vermelho, verde, cinza, laranja)
from prettytable import PrettyTable

# import random


aba1 = "PID"
aba2 = "ARQ"
aba3 = "REDE1"
aba4 = "REDE2"
titulo_abas = [aba1, aba2, aba3, aba4]

# Inicialização da fonte
pygame.font.init()
terminou = False


# Dimensões da tela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

dicionario = {'alexandre': 456123789, 'anderson': 1245698456,
              'antonio': 123456456, 'carlos': 91257581,
              'cesar': 987458, 'rosemary': 789456125}


# Soma e Cálcula as Médias das chaves dos dicionários em MB
valores_Bytes = dicionario.values()
soma = sum(dicionario.values())
soma = soma / 1024 / 1024
soma_media = soma / len(dicionario)


class Abas():
    def __init__(self):
        self.largura = 200
        self.altura = 50
        self.x = 0
        self.y = 20
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = verde
        self.titulo = titulo_abas[0]


    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)


# Converte os valores das chaves do dicionário em MB
for i in dicionario.keys():
    valor = dicionario[i]
    converter_mb = valor / 1024 / 1024
    dicionario[i] = round(converter_mb, 2)


def mostra_titulo():
    font = pygame.font.Font(None, 24)
    text = font.render("Teste", 1, preto)
    textpos = text.get_rect(centerx=tela.get_width() / 2, centery=20)
    tela.blit(text, textpos)


def mostra_aba_1():
    q = Abas()
    q.area = pygame.Rect(0, 40, 200, 50)
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[0], 1, branco)
    textpos = text.get_rect(centerx=q.x + 100, centery=q.y + 45)
    q.desenha(tela)
    tela.blit(text, textpos)


def mostra_aba_2():
    q = Abas()
    q.area = pygame.Rect(200, 40, 200, 50)
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[1], 1, branco)
    textpos = text.get_rect(centerx=q.x + 300, centery=q.y + 45)
    q.desenha(tela)
    tela.blit(text, textpos)

def mostra_aba_3():
    q = Abas()
    q.area = pygame.Rect(400, 40, 200, 50)
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[2], 1, branco)
    textpos = text.get_rect(centerx=q.x + 500, centery=q.y + 45)
    q.desenha(tela)
    tela.blit(text, textpos)


def mostra_aba_4():
    q = Abas()
    q.area = pygame.Rect(600, 40, 200, 50)
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[3], 1, branco)
    textpos = text.get_rect(centerx=q.x + 700, centery=q.y + 45)
    q.desenha(tela)
    tela.blit(text, textpos)


def mostra_titulo_h2(texto, y):
    font = pygame.font.Font(None, 20)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(center=(tela.get_width() / 2, y + 20))
    tela.blit(text, textpos)


def formata_valores(dicionario, soma):
    soma_indices = 1

    for i in dicionario.keys():
        dicionario[i] = round(dicionario[i], 2)
        porcentagem = round((dicionario[i] / soma) * 100, 2)
        p = f'{soma_indices:>10} {i:^10} {dicionario[i]:^30,.2f} {porcentagem:^40,.2f}'
        mostra_titulo_h2(p, 150 + soma_indices * 30)
        soma_indices = soma_indices + 1


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    pygame.draw.rect(tela, laranja, (20, 550, larg, 35))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, azul_2, (20, 550, larg, 35))


tela.fill(cinza)
mostra_titulo()
mostra_aba_1()
mostra_aba_2()
mostra_aba_3()
mostra_aba_4()
mostra_titulo_h2("ACME Inc. Uso do espaço em disco pelos usuários", 100)
mostra_titulo_h2("Nr.        Usuário        Espaço Utilizado        % do uso", 130)
formata_valores(dicionario, soma)
mostra_titulo_h2(f"Total de memoria usada: {round(soma, 2)} Mb", 400)
mostra_titulo_h2(f"Media de memoria usada: {round(soma_media, 2)} Mb", 450)
mostra_uso_memoria()


while not terminou:

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtém as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()
            # Checa se clicou em algum dos quadrados
            # for q in lista:
            #     if q.area.collidepoint(pos):
            #         lista.append(q)
            #         print(lista)
            #         # pontos = pontos + 1

        if event.type == pygame.QUIT:
            terminou = True

    # Atualiza o desenho na tela
    pygame.display.update()
# Finaliza a janela do jogo
pygame.display.quit()
