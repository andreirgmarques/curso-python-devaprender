# DateTime e Tempo
from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data 
lancamento_app = datetime(2022, 5, 9)
print(lancamento_app)

# Receber data de lançamento do meu aplicativo
data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'), '%d/%m/%Y')
print(type(data_de_lancamento))

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)


# Desafio
aniversario = datetime(2023, 2, 20)
dias_para_aniversario = aniversario - datetime.now()
print(dias_para_aniversario.days)