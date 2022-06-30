# Enumerate
for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metada da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    
    
# Desafio
frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(indice, f'{fruta} EM PROMOÇÃO')
    else:
        print(indice, fruta)