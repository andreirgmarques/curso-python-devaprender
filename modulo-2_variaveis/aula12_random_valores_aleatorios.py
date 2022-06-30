# Valores aleatórios com random
import random

# Gera um valor aleatório de 0.0 a 1.0
print(random.random()) 

# Gera um valor decimal de Valor Mínimo ao Valor Máximo
print(random.uniform(4, 10))

# Gera um valor inteiro de Valor Mínimo ao Valor Máximo
print(random.randint(4, 10))

# Escolher uma opção aleatória
cores = ['verde', 'vermelho', 'azul']
print(random.choices(cores, k=2))

# Embaralhar uma lista
cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

# Desafio 1
lados_moeda = ['cara', 'coroa']
print(random.choice(lados_moeda))

# Desafio 2
nomes = ['andrei', 'ricardo', 'gomes', 'marques', 'eva']
print(random.choice(nomes))

# Desafio 3
print(random.randint(10, 100))