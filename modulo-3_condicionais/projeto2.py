from turtle import Turtle

# Inicializar uma turtle
t = Turtle()

# Definir a velocidade
t.speed(1)

finaliza_execucao = False
while not finaliza_execucao:
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás"')
    direcao_msg = 'frente' if direcao == 'f' else 'trás'
    pixels = int(input(f'Quantos pixels devemos movimentar para {direcao_msg}?'))
    rotacao = input('Rotacionar para "d:direita", "e:esquerda" ou "n:não rotacionar"?')
    graus = 0
    if rotacao == 'd' or rotacao == 'e':
        rotacao_msg = 'direita' if rotacao == 'd' else 'esquerda'
        graus = float(input(f'Quanto para {rotacao_msg} devemos rotacionar?'))
    if rotacao == 'd':
        t.right(graus)
    elif rotacao == 'e':
        t.left(graus)
    if direcao == 'f': 
        t.forward(pixels)
    else:
        t.backward(pixels)
    finaliza_execucao = input('Continua andando?') == 'n' 