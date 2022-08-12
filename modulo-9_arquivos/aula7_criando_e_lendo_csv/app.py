import os
from csv import DictReader, DictWriter

os.chdir('modulo-9_arquivos')
os.chdir('aula7_criando_e_lendo_csv')

# with open(os.getcwd() + os.sep + 'csv_exemplo.csv', 'r') as arquivo:
#     dados = arquivo.read()
#     print(dados)

# Ler um arquivo CSV
# with open(os.getcwd() + os.sep + 'csv_exemplo.csv', 'r') as arquivo:
#     dados = DictReader(arquivo)
#     for dado in dados:
#         print(dado['Id'] + ' ' + dado['Age'])

# Criar um arquivo CSV
# with open(os.getcwd() + os.sep + 'computadores.csv', 'w', newline='', encoding='utf-8') as arquivo:
#     cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
#     csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         'Marca': 'Asus',
#         'Preço': 2500,
#         'Ano de Lançamento': 2010
#     })
#     csv_writer.writerow({
#         'Marca': 'Asus',
#         'Preço': 2500,
#         'Ano de Lançamento': 2010
#     })
#     csv_writer.writerow({
#         'Marca': 'Asus',
#         'Preço': 2500,
#         'Ano de Lançamento': 2010
#     })
#     csv_writer.writerow({
#         'Marca': 'Asus',
#         'Preço': 2500,
#         'Ano de Lançamento': 2010
#     })

# Criar um arquivo CSV
with open(os.getcwd() + os.sep + 'computadores.csv', 'r', newline='',
          encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    computadores = list(dados_originais)
    with open(os.getcwd() + os.sep + 'computadores_v2.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
        cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for computador in computadores:
            csv_writer.writerow({
                'Marca': computador['Marca'],
                'Preço': 'R$' + computador['Preço'],
                'Ano de Lançamento': computador['Ano de Lançamento']
            })
