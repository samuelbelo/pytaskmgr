# coding=utf-8
import psutil

mem = psutil.virtual_memory()
capacidade = round(mem.total / (1024*1024*1024), 2)

print('Total de memoria: ', capacidade, 'GB')
