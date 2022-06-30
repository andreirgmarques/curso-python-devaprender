# Try Finally
try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero!')
except ValueError as erro:
    print('Favor digitar apenas números!')
finally:
    print('A operação foi cancelada')
