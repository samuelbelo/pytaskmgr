from prettytable import PrettyTable

# Cria a tabela
x = PrettyTable(["Nome da cidade", "UF", "População", "IDH-M", "Renda per Capita"])

# Alinha as colunas
x.align["Nome da cidade"] = "l"
x.align["UF"] = "l"
x.align["População"] = "r"
x.align["IDH-M"] = "r"
x.align["Renda per Capita"] = "r"

# Deixa um espaço entre a borda das colunas e o conteúdo (default)
# x.padding_width = 1
#
# x.add_row(["São Paulo","SP", 12106920, 0.805, 54358])
# x.add_row(["Rio de Janeiro","RJ", 6520266, 0.799, 49527])
# x.add_row(["Belo Horizonte", "MG", 2523794, 0.810, 35187])
# x.add_row(["Porto Alegre", "RS", 1484941, 0.805, 46122])
# x.add_row(["Salvador", "BA", 2953986, 0.759, 19812])
# x.add_row(["Recife", "PE", 1633697, 0.772, 29701])
# x.add_row(["Brasília", "DF", 3039444, 0.824, 73971])

x = PrettyTable()
x.add_column('Nome da cidade', ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador", "Recife", "Brasília"])
x.add_column('UF', ["SP", "RJ", "MG", "RS", "BA", "PE", "DF"])
x.add_column('População', [12106920, 6520266, 2523794, 1484941, 2953986, 1633697, 3039444])
x.add_column('IDH-M', [0.805, 0.799, 0.811, 0.805, 0.759, 0.772, .0824])
x.add_column('Renda per Capita', [54358, 49527, 35187, 46122, 19812, 29701, 73971])

print(x)