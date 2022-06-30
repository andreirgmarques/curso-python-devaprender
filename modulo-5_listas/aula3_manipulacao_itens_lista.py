# Manipulação de itens de uma lista

valores = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]

# Adicionar ao final da lista
# valores.append(11)
print(valores)

# Unir listas
# valores.extend(anos)
print(valores)

# Adicionar listas
nova_lista = valores + anos
print(nova_lista)

# Inserir
print(anos[1])
anos.insert(2, 2031)
print(anos)

# Extrais com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)

# Remover item da lista
# anos.remove(2050)
# del valores[1:6]
print(valores)

# Contar ocorrências de items
print(valores.count(2))

# Resetar
valores.clear()
print(valores)