# Lidando com Arquivos JSON
import json
from pathlib import Path

# carros = [
#     {"marca": "Nissan", "preco": 45.000, "cor": "Azul"},
#     {"marca": "Ford", "preco": 75.000, "cor": "Verde"},
#     {"marca": "BMW", "preco": 117.000, "cor": "Amarelo"}
# ]
# carros_json = json.dumps(carros)
# Path('carros.json').write_text(carros_json, encoding='UTF-8')

arquivo_carros_json = Path('carros.json').read_text(encoding='UTF-8')
arquivo_json = json.loads(arquivo_carros_json)
print(arquivo_json[0]['marca'] + ' ' + str(arquivo_json[0]['preco']))
print(arquivo_json[1]['marca'] + ' ' + str(arquivo_json[1]['preco']))
