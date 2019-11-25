import pygame
import os
import time
import psutil
from dicionario import *
from cores import *
from aba3 import *
#from aba4 import *
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


def mostra_titulo(tela, texto, x, y):
    font = pygame.font.Font(None, 26)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=x + 100, centery=y + 155)
    textpos.left = x
    tela.blit(text, textpos)


def desenha_abas():
    for i in range(4):
        x = i * 300
        # pygame.draw.rect(tela, darkBlue, (x, 50, 200, 50), 0)
        a = pygame.draw.rect(tela, darkBlue, (x, 50, 300, 50), 0)
        pygame.draw.rect(tela, branco, (x, 50, 300, 50), 1)
        mostra_titulo_abas(i, x)
        lista.append(a)


def mostra_titulo_abas(i, x):
    font = pygame.font.Font(None, 24)
    text = font.render(titulo_abas[i], 1, branco)
    textpos = text.get_rect(centerx=x + 150, centery=75)
    tela.blit(text, textpos)


def mostra_titulo_h2(tela, texto, x, y):
    font = pygame.font.Font('OpenSans-Regular.ttf', 14)
    text = font.render(texto, 1, preto)
    textpos = text.get_rect(centerx=x + 100, centery=y+150)
    textpos.left = x
    tela.blit(text, textpos)


caminho_pasta = os.getcwd()
arquivo = os.listdir(caminho_pasta)
titulo_arquivo = ['Arquivo', 'Tamanho', 'Criado em', 'Última Modificação']


def conteudo_aba0():
    soma = 1
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
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
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_ctime))}',
                                    x=400, y=soma * 30)
        mostra_titulo_h2(tela, f'{time.strftime("%d/%m/%Y     %H:%M:%S", time.localtime(status_arquivo.st_mtime))}',
                                    x=600, y=soma * 30)
        soma += 1
        os.times()


soma_rss = sum([i["RSS"] for i in lista_dicionarios])/1024/1024/1024
soma_vms = sum([i["VMS"] for i in lista_dicionarios])/1024/1024/1024
soma = 0
soma_media = 0
titulo_conteudo_aba1 = ['Processo', 'Nome', 'Tamanho vms', 'Tamanho rss', '% vms', '% rss']
titulo_conteudo_aba2 = ['PID', 'End.', 'Tipo', 'Status', 'Endereço Local', 'Porta L.', 'Endereço Remoto', 'Porta R.']


def conteudo_aba1():
    soma_indices = 1
    # mostra_tempo(tempo, minuto)
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
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



'''                       0      1        2        3             4              5               6              7    '''
titulo_conteudo_aba2 = ['PID', 'End.', 'Tipo', 'Status', 'Endereço Local', 'Porta L.', 'Endereço Remoto', 'Porta R.']


def conteudo_aba2():
    print(lista_raddr)
    soma_indices = 1
    # mostra_tempo(tempo, minuto)
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    mostra_titulo(tela, titulo_conteudo_aba2[0], 50, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[1], 150, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[2], 200, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[3], 250, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[4], 350, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[5], 650, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[6], 750, -40)
    mostra_titulo(tela, titulo_conteudo_aba2[7], 1100, -40)

    for i in range(len(lista_pid)):
        p = psutil.Process(lista_pid[i])
        conn = p.connections()
        mostra_titulo_h2(tela, f'{p.pid}', 50, -30 + soma_indices * 22)

        for t in range(len(conn)):
            mostra_titulo_h2(tela, f'{obtem_nome_familia(conn[t].family)}', 150, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{obtem_tipo_socket(conn[t].type)}', 200, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{conn[t].status}', 250, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].laddr[0])}', 350, -30 + soma_indices * 22)
            mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].laddr[1])}', 650, -30 + soma_indices * 22)
            if obtem_dados_conexao_remota(conn[t].raddr) != '-':
                mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].raddr[0])}', 750, -30 + soma_indices * 22)
                mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].raddr[1])}', 1100, -30 + soma_indices * 22)
            else:
                mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].raddr)}', 750, -30 + soma_indices * 22)
                mostra_titulo_h2(tela, f'{obtem_dados_conexao_local(conn[t].raddr)}', 1100, -30 + soma_indices * 22)
            soma_indices += 1

def conteudo_aba4():
    soma_indices = 1
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    mostra_titulo_h2(tela, "Gráfico de Processos PID x VMS", 500, -40)
    processos_infos = []
    for processos in psutil.process_iter():
        processos_infos.append(
            {"pid" :processos.pid,
             "nome" : processos.name(),
             "rss" : processos.memory_info().rss,
             "vms" : processos.memory_info().vms})
    names = [info["pid"] for info in processos_infos]
    values = [info["vms"]/1024/1024 for info in processos_infos]
    
    fig, axs = plt.subplots()
    lines, = axs.plot(names, values)
    plt.xlabel("pid")
    plt.ylabel("vms")
    plt.setp(lines, color = 'b', linewidth=1.0)
    fig.suptitle('PID X VMS')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    tamanho = canvas.get_width_height()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    superficie_grafico = pygame.image.fromstring(raw_data, tamanho, "RGB")
    tela.blit(superficie_grafico, (280,200))


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
                        conteudo_aba2()
                        # mostra_titulo_aba3('Vai que colaaaaaaaaaaa?!')
                        break
                    elif q == lista[3]:
                        aba1 = False
                        conteudo_aba4()
                        break
    #tela.scroll(10,10)
    #tela.blit(area,((200 + 5) % 720, (200 + 5) % 720))

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
