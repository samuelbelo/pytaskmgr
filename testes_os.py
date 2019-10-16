import os

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
