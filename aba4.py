from dicionario import *

def grafico():
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use("Agg")
    import matplotlib.backends.backend_agg as agg
    dicionario = lista_dicionarios
    names = list(dicionario.keys())
    values = list(dicionario.values())

    fig, axs = plt.subplots()
    axs.plot(names, values)
    fig.suptitle('Categorical Plotting')

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    tamanho = canvas.get_width_height()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    superficie_grafico = pygame.image.fromstring(raw_data, size, "RGB")
    tela.blit(surf, (0,150))