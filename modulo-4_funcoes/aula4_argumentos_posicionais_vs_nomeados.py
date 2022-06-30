# Argumentos Posicionais vs Argumentos Nomeados

# Define a função para aceitar somente argumentos nomeados depois do *
# def exibir_preco(nome_produto, *, preco):
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

# Argumentos Posicionais
exibir_preco('Iphone', 5000)

# Argumentos Nomeados
exibir_preco(nome_produto='Iphone', preco=5000)
