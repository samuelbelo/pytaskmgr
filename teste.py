import psutil
lista_dicionarios = []
soma_indices = 1
soma_rss = sum([i["rss"] for i in lista_dicionarios])/1024/1024/1024
soma_vms = sum([i["vms"] for i in lista_dicionarios])/1024/1024/1024
soma = 0
soma_media = 0
for p in psutil.process_iter():
    lista_dicionarios.append(
        {"Pid" : p.pid,
         "Nome": p.name,
         "RSS": p.memory_info().rss,
         "VMS": p.memory_info().vms,
         "Status": p.status()})
print(lista_dicionarios)
