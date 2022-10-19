import os

# import shutil

# Listar arquivos
# arquivos = os.listdir("C:\\python")
# print(arquivos)

# caminho da pasta atual
# caminho = os.getcwd()
# print(caminho)

# renomear
# os.rename('C:\\python\\Vendas - 1.xlsx', 'C:\\python\\Vendas 1.xlsx')

# mover
# os.rename('C:\\python\\Vendas - 1.xlsx',
#           'C:\\python\\vendas\\Vendas - 1.xlsx')

# copiar arquivos
# shutil.copy2('C:\\python\\Vendas - 1.xlsx',
#             'C:\\python\\vendas\\Vendas 1.xlsx')

# Aplicação
arquivos = os.listdir("C:\\python")

for arquivo in arquivos:
    if 'xlsx' in arquivo:
        if 'Compras' in arquivo:
            os.rename(f'C:\\python\\{arquivo}',
                      f'C:\\python\\Compras\\{arquivo}')
        elif 'Vendas' in arquivo:
            os.rename(f'C:\\python\\{arquivo}',
                      f'C:\\python\\Vendas\\{arquivo}')
