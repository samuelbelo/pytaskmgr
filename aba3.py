import psutil
import time
import socket


def obtem_nome_familia(familia):
    if familia == socket.AF_INET:
        return "IPv4"

    elif familia == socket.AF_INET6:
        return "IPv6"

    elif familia == socket.AF_UNIX:
        return "Unix"

    else:
        return " - "


def obtem_tipo_socket(tipo):
    if tipo == socket.SOCK_STREAM:
        return 'TCP'

    elif tipo == socket.SOCK_DGRAM:
        return 'UDP'

    elif tipo == socket.SOCK_RAW:
        return 'IP'

    else:
        return '-'


def obtem_dados_conexao_local(laddr):
    if laddr != ():
        return laddr

    else:
        return '-'


def obtem_dados_conexao_remota(raddr):
    if raddr != ():
        return raddr

    else:
        return '-'


lista_pid = []

for i in psutil.net_connections():
    lista_pid.append(i.pid)

