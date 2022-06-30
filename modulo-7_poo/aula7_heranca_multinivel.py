# Herança multinível

# 1º Problema
class Veiculo:
    pass
class VeiculoDeRoda(Veiculo):
    pass
class Carro(VeiculoDeRoda):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass
