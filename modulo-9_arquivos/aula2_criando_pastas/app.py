import os

os.chdir('modulo-9_arquivos')
os.chdir('aula2_criando_pastas')

# os.mkdir('Musicas') # Criar uma pasta não existente
# os.makedirs('Videos' + os.sep + 'Ação') # Criar pastas e subpastas
# os.makedirs('Musicas' + os.sep + 'Rock')

if not os.path.isdir('Musicas'):
    os.mkdir('Musicas')
else:
    print('Diretório já existe')
