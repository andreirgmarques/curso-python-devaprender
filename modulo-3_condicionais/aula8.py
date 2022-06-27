# if elif else

# trabalho_terminado = False
# if trabalho_terminado:
#     print('Bora dar uma saída!')
# else:
#     print('Não posso sair agora.')    

# numero_atrasos = 2
# if numero_atrasos >= 3:
#     print('Vá para a diretoria')
# elif numero_atrasos == 2:       
#     print('Essa é a sua segunda falta')
# elif numero_atrasos == 1:
#     print('Essa é a sua primeira falta')
# else:
#     print('Pode entrar')


'''
A velocidade máxima para essa rua é 50km
* Cruzou entre 50km a 60km, levou multa de 2 pontos
* Cruzou entre 61km a 75km, levou multa de 3 pontos
* Cruzou acima de 75km, levou multa de 7 pontos
'''
# velocidade = 100
# if velocidade <= 50:
#     print('Não foi multado')
# elif velocidade >= 51 and velocidade <= 60:
#     print('Levou multa de 2 pontos')
# elif velocidade >= 61 and velocidade <= 75:
#     print('Levou multa de 3 pontos')
# else:
#     print('Levou multa de 7 pontos')

# Versão Chaining    
velocidade = 100
if velocidade <= 50:
    print('Não foi multado')
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif 61 <= velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos')    