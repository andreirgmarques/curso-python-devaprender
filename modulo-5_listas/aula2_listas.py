# Criando listas com Python

# Listas
precos = [10, 20, 30, 40, 50, 60, 100, 250, 230, 560, 23, 74]
print(precos[0]) # Acesso por índice
print(precos[precos.index(100)])

# Listas no python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 2, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])



# Maneiras diferentes de gerar uma lista

# Multiplicação de valores (repetição)
lista_de_noves = [9] * 10
print(lista_de_noves)

lista_de_teste = ['teste'] * 10
print(lista_de_teste) 

# Usando gerador (range)
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de string
print(list('Bem-vindo ao treinamento'))

# Lista de lista (matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])
