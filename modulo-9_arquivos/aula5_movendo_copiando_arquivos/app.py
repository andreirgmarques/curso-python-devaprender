import shutil
import os

os.chdir('modulo-9_arquivos')
os.chdir('aula5_movendo_copiando_arquivos')

# Copia arquivos entre pastas
# shutil.copy(src=os.getcwd() + os.sep + 'fotos' + os.sep + 'foto1.jpg',
#             dst=os.getcwd() + os.sep + 'backup')

# Copia pasta completa para outra pasta
# shutil.copytree(src=os.getcwd() + os.sep + 'fotos',
#                 dst=os.getcwd() + os.sep + 'fotos_backup')

# Move arquivos ou pastas para outra pasta
# shutil.move(src=os.getcwd() + os.sep + 'fotos' + os.sep + 'foto2.jpg',
#             dst=os.getcwd() + os.sep + 'backup')
# shutil.move(src=os.getcwd() + os.sep + 'fotos_backup',
#             dst=os.getcwd() + os.sep + 'backup')

# Apaga pasta com seu conteúdo
# shutil.rmtree(path=os.getcwd() + os.sep + 'musicas')

# Compacta arquivos ou pastas
# shutil.make_archive('backup_fotos', 'zip', os.getcwd() + os.sep + 'fotos')
# shutil.make_archive('backup_vs_code', 'zip', os.getcwd())

# Descompacta arquivos ou pastas
shutil.unpack_archive('backup_vs_code.zip', os.getcwd() + os.sep + 'backup_vs_code')
