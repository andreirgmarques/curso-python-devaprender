# Dicionários (chave, valor)

dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
print(dicionario_pessoa)

# pessoa2 = dict(nome='Carol', idade=18, altura=1.60)
# print(pessoa2)

# Imprimir propriedade do dicionário
print(dicionario_pessoa['idade'])

# Imprimir chaves disponíveis no dicionário
print(dicionario_pessoa.keys())

# Imprimir valores no dicionário
print(dicionario_pessoa.values())

# Imprimir items no dicionário
print(dicionario_pessoa.items())

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item[1])
