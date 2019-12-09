import pygame
from cores import cinza
from dicionario import *


def grafic(tela):
    # soma_indices = 1
    import matplotlib
    import matplotlib.pyplot as plt
    pygame.draw.rect(tela, cinza, (0, 0, 1200, 800), 0)
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    processos_infos = []
    for processos in psutil.process_iter():
        processos_infos.append(
            {"pid": processos.pid,
             "nome": processos.name(),
             "rss": processos.memory_info().rss,
             "vms": processos.memory_info().vms})
    names = [info["pid"] for info in processos_infos]
    values1 = [info["vms"] / 1024 / 1024 for info in processos_infos]
    values2 = [info["rss"] / 1024 / 1024 for info in processos_infos]

    fig_1, axs = plt.subplots()
    lines_1, = axs.plot(names, values1)
    plt.xlabel("pid")
    plt.ylabel("vms")
    plt.setp(lines_1, color='b', linewidth=1.0)
    fig_1.suptitle('PID X VMS')

    fig_2, axs = plt.subplots()
    lines_2, = axs.plot(names, values2)
    plt.xlabel("pid")
    plt.ylabel("rss")
    plt.setp(lines_2, color='b', linewidth=1.0)
    fig_2.suptitle('PID X RSS')

    canvas_1 = agg.FigureCanvasAgg(fig_1)
    canvas_1.draw()
    tamanho_1 = canvas_1.get_width_height()
    renderer = canvas_1.get_renderer()
    raw_data_1 = renderer.tostring_rgb()

    canvas_2 = agg.FigureCanvasAgg(fig_2)
    canvas_2.draw()
    tamanho_2 = canvas_2.get_width_height()
    renderer = canvas_2.get_renderer()
    raw_data_2 = renderer.tostring_rgb()

    superficie_grafico_1 = pygame.image.fromstring(raw_data_1, tamanho_1, "RGB")
    tela.blit(superficie_grafico_1, (0, 150))

    superficie_grafico_2 = pygame.image.fromstring(raw_data_2, tamanho_2, "RGB")
    tela.blit(superficie_grafico_2, (590, 150))
