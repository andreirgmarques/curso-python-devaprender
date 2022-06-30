# Mantendo um log(histórico) de exceções
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digie seu e-mail: ')
    senha = int(input('Digite sua senha bancária: '))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info('%s entrou em sua conta bancária.', email)
except ValueError as erro:
    print('Digite apenas números!')
    logging.error(erro)
