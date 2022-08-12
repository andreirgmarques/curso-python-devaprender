"""
COMO CRIAR E MODIFICAR ARQUIVOS:
'w' -> Usado somente para escrever algo
'a' -> Usado para acrescentar algo
'r' -> Usado somente para ler algo
'r+' -> Usado para ler e escrever algo
"""

import os

os.chdir('modulo-9_arquivos')
os.chdir('aula3_salvando_informacoes_em_arquivos')

# with open('celulares.txt', 'w') as arquivo:
#     arquivo.write('Celular 2')

# nomes = ['lucas', 'carol', 'jeff', 'douglas']
# with open('nomes.txt', 'a', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)

# numeros = [1, 2, 3, 4, 5, 6]
# with open('numeros.txt', 'a', newline='') as arquivo:
#     for numero in numeros:
#         arquivo.write(str(numero) + os.linesep)

# with open('nomes.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha)

# with open('numeros.txt', 'r+') as arquivo:
#     for linha in arquivo:
#         print(linha)
#     arquivo.write('9000')
