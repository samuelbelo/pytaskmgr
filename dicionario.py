import psutil

lista_dicionarios = []

for p in psutil.process_iter():
    lista_dicionarios.append(
        {"Pid": p.pid,
         "Nome": p.name,
         "RSS": p.memory_info().rss,
         "VMS": p.memory_info().vms,
         "Status": p.status()})
