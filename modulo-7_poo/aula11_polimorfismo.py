# Polimorfismo
# class Carro:
#     def ligar(self):
#         print('Ligando o carro')


# class Moto:
#     def ligar(self):
#         print('Ligando a moto')


# def iniciar(veiculo):
#     veiculo.ligar()


# carro = Carro()
# moto = Moto()

# iniciar(carro)
# iniciar(moto)


class Pessoa:
    def apresentar(self, nome, idade = None, profissao = None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)


pessoa = Pessoa()
pessoa.apresentar(nome='Andrei', idade=29, profissao='Programador')
pessoa.apresentar(nome='Andrei', idade=29)
pessoa.apresentar(nome='Andrei', profissao='Programador')
pessoa.apresentar(nome='Andrei')
