import os
import time
import pygame
from cores import *
from funcoes_globais import mostra_titulo_h2
from funcoes_globais import tela

caminho_pasta = os.getcwd()
arquivo = os.listdir(caminho_pasta)
titulo_arquivo = ['Arquivo', 'Tamanho', 'Criado em', 'Última Modificação']


def conteudo_1():
    soma = 1
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    mostra_titulo_h2(tela, f'{titulo_arquivo[0]}', x=25, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[1]}', x=200, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[2]}', x=400, y=5)
    mostra_titulo_h2(tela, f'{titulo_arquivo[3]}', x=600, y=5)

    for i in range(len(arquivo)):
        status_arquivo = os.stat(f'{arquivo[i]}')
        mostra_titulo_h2(tela, f'{arquivo[i]}', x=25, y=soma * 30)
        mostra_titulo_h2(tela, f'{status_arquivo.st_size/1024:.2f} KBytes', x=200, y=soma *30)
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_ctime))}',
                         x=400, y=soma * 30)
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_mtime))}',
                         x=600, y=soma * 30)
        soma += 1
        os.times()
