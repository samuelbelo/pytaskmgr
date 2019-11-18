import psutil
import time
import socket

# interfaces = psutil.net_if_addrs()
# nomes = []
#
# # Obtém os nomes das interfaces primeiro
# for i in interfaces:
#     nomes.append(str(i))
#
# # Depois, imprimir os valores:
# for i in nomes:
#     print(i+":")
#     for j in interfaces[i]:
#         print("\t"+str(j))
#
# print("<-------------------------------------------- Fim 1 ---------------------------------------------------------->")
#
# status = psutil.net_if_stats()
# for i in nomes:
#     print(i)
#     print("\t"+str(status[i]))
#
# print("<-------------------------------------------- Fim 2 ---------------------------------------------------------->")
#
# for i in range(5):
#     print(psutil.net_io_counters())
#     time.sleep(1)
#
# print("<-------------------------------------------- Fim 3 ---------------------------------------------------------->")
#
# io_status = psutil.net_io_counters(pernic=True)
# nomes = []
#
# for i in io_status:
#     nomes.append(str(i))
#
# for j in nomes:
#     print(j)
#     print("\t"+str(io_status[j]))
#
# for i in range(4):
#     time.sleep(1)
#     io_status = psutil.net_io_counters(pernic=True)
#
#     for j in nomes:
#         print(j)
#         print("\t"+str(io_status[j]))
#
# print("<------------------------------------------- Fim 4 --------------------------------------------------------->")

# for i in psutil.net_connections():
#     print(i)
#
# print("<------------------------------------------- Fim 5 --------------------------------------------------------->")


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
        print(laddr)

    else:
        return '-'
        # return '-'


lista_raddr = []


def obtem_dados_conexao_remota(raddr):
    if raddr != ():
        return raddr

    else:
        return '-'


lista_pid = []

for i in psutil.net_connections():
    lista_pid.append(i.pid)

# print(lista_pid)

# print(teste)

# print("-------------------------------------------------Projeto-------------------------------------------------------")

for i in range(len(lista_pid)):
    p = psutil.Process(lista_pid[i])
    conn = p.connections()
    print(conn)

    print("-----------------------------------------------------------------------------------------------------------")
    print(f'Processo: {p.pid}')
    print("-----------------------------------------------------------------------------------------------------------")
    for t in range(len(conn)):
        obtem_nome_familia(conn[t].family)
        obtem_tipo_socket(conn[t].type)
        # print(f'Status: {conn[t].status}')
        obtem_dados_conexao_local(conn[t].laddr)
        obtem_dados_conexao_remota(conn[t].raddr)
#
#
# print(lista_raddr)
# print("------------------------------------------------------------------------------------------------------------")

# print("------------------------------------------------------------------------------------------------------------")

