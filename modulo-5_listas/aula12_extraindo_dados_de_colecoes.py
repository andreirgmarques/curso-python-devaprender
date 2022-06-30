# Extraindo dados de coleções existentes

# Criar listas usando loops e range
# numeros = []
# for i in range(5):
#     numeros.append(i)
# print(numeros)

# Criar listas usando Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
def aprovar_pessoas(nome):
    return nome + ' APROVADO'
print(list(map(aprovar_pessoas, nomes)))
