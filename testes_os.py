import os, time

print(os.environ['HOMEDRIVE'])
print(os.environ['HOMEPATH'])
print(os.getlogin())
print(os.name)
print(os.getcwd())
print(os.getpid())
# diretorio = f'{os.getpid()}'
# os.mkdir('Projeto de Bloco')
# os.rename('Projeto de Bloco', 'Projeto de Bloco2')
# os.rmdir('Projeto de Bloco2')
# print(os.listdir(os.chdir('..')))
print(os.path.exists('.idea'))
print(os.path.isfile('os_instruções.txt'))
print(os.path.basename('D:\\Faculdade\\Graduação\Python\\Projeto de Bloco'))
print(os.path.dirname('D:\\Faculdade\\Graduação\Python\\Projeto de Bloco\\os_instruções.txt'))
print(os.path.abspath('os_instruções.txt'))
print(os.path.split('D:\\Faculdade\\Graduação\Python\\Projeto de Bloco\\os_instruções.txt'))
print('\n')
p = os.path.abspath('os_instruções.txt')
t = os.path.split(p)            # separa em duas partes
p0 = t[0]                       # parte 0
p1 = t[1]                       # parte 1
lista_dir = []
while p1:                       # fazer enquanto houver parte 1
    lista_dir.append(p1)        # adiciona à lista a parte 1
    t = os.path.split(p0)       # agora, separa p0
    p0 = t[0]
    p1 = t[1]
lista_dir.append(p0)            # Colocar último
lista_dir.reverse()             # Para reverter a lista, pois ela estava ao contrário
print(lista_dir)                # imprime a lista
print(os.path.join('D:', 'Faculdade', 'Graduação', 'Python', 'Projeto de Bloco', 'os_instruções.txt'))
print(os.path.join(os.getcwd(), 'os_instruções.txt'))
status = os.stat('os_instruções.txt')
print(status.st_size, 'bytes')
status = os.stat('os_instruções.txt')
print(time.ctime(status.st_mtime))

arquivos = f'{os.getcwd()}'
print(os.listdir(arquivos))
arquivo = os.listdir(arquivos)
def teste():
    for i in range(len(arquivo)):
        teste = os.stat(f'{arquivo[i]}')
        resultado = (arquivo[i], teste.st_size, time.ctime(teste.st_atime), time.ctime(teste.st_mtime))

        print(resultado)

teste()