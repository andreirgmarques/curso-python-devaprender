# Tuplas são listas que não podem ser modificadas

# Criação da Tupla
sites = ('youtube.com', 'facebook.com', 'instagram.com', 54, True)
valores = (23, 43, 65, False)
print(sites[1])
print(valores[2])
 
# União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)

# Acesso de valores em uma tupla
print(dados_do_sistema[2])
 