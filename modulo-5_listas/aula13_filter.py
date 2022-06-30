# Filter
# nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
# def pessoa_aprovada(pessoa):
#     if pessoa == 'Marcus':
#         return True
#     else:
#         return False
# print(list(filter(pessoa_aprovada, nomes)))

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Classica', 'Verde', 1897]
]
def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
print(list(filter(eh_antiguidade, pinturas)))
