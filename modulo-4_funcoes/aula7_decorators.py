# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns!!!')

parabenizar()


# Desafio
from datetime import datetime

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario
def baixar_musicas():
    print('Baixando Músicas...')

baixar_musicas()