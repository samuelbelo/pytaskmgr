from dicionario import *
import pygame
from cores import cinza

def grafic(tela):
    soma_indices = 1
    import matplotlib
    import matplotlib.pyplot as plt
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    processos_infos = []
    for processos in psutil.process_iter():
        processos_infos.append(
            {"pid" :processos.pid,
             "nome" : processos.name(),
             "rss" : processos.memory_info().rss,
             "vms" : processos.memory_info().vms})
    names = [info["pid"] for info in processos_infos]
    values1 = [info["vms"]/1024/1024 for info in processos_infos]
    values2 = [info["rss"]/1024/1024 for info in processos_infos]
    
    fig, axs = plt.subplots()
    lines, = axs.plot(names, values2)
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
    tela.blit(superficie_grafico, (5, 150))
    
    superficie_grafico = pygame.image.fromstring(raw_data, tamanho, "RGB")
    tela.blit(superficie_grafico, (610, 150))