import os

print(os.name) # Retorna Nome do Sistema Operacional
print(os.listdir()) # Lista arquivos no diretório atual
print(os.getcwd()) # Retorna caminho do diretório atual
print(os.sep) # Retorna separador de pastas nativo do sistema operacional
print(os.path.join(os.getcwd() + os.sep + 'senhas.txt')) # Retorna pasta do arquivo senhas.txt
print(os.path.join(os.getcwd() + os.sep + 'documentos' + os.sep + 'senhas.txt')) # Retorna pasta do arquivo musica.mp3

caminho_senha = os.path.join(os.getcwd() + os.sep + 'senhas.txt')
print(os.path.dirname(caminho_senha)) # Retorna diretório de um caminho de arquivo
print(os.path.basename(caminho_senha)) # Retorna nome do arquivo
print(os.path.exists(os.getcwd() + os.sep + 'documentos'))

os.chdir('modulo-9_arquivos') # Navega para pasta modulo-9_arquivos
print(os.getcwd())
os.chdir('..') # Navega para pasta anterior
print(os.getcwd())
