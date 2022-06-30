# Trabalhando com múltiplas listas usando o ZIP
from itertools import zip_longest

a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5, 6]
for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]
for produto, preco in zip(produtos, precos):
    print(f'Salvando produto {produto} valor R$ {preco}')
    
titulos = ['Título 1', 'Título 2', 'Título 3', 'Título 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} com a descrição: {descricao}')
