# Log e Logging
import logging

from isort import file

'''
DEBUG - Só estou informando informações para desenvolvedores.
INFO - Só quero informar algo que está acontecendo no programa, mas que não é um erro.
WARNING - Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, porém ainda
          não é um erro, mas pode gerar um futuramente.
ERROR - Um erro ocorreu na aplicação.
CRITICAL - Um erro com consequências graves acaba de ocorrer na aplicação.
'''

logging.basicConfig(level=logging.DEBUG, filename='./aula5.log', filemode='a', format='%(levelname)s - %(message)s') # Setar o nível padrão do log
logging.debug('Logging no nível debug')
logging.info('Logging no nível info')
logging.warning('Logging no nível warning')
logging.error('Logging no nível error')
logging.critical('Logging no nível critical')
