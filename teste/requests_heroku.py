"""

Testando a requisição da API. Esta API vai retornar o foi enviando, caso a
chave de autorização seja 42.

Aqui você vai precisar instalar a lib requests

    pip install requests

"""

import json
from requests import get

url = 'https://deployapi.herokuapp.com/'

data = {
    "language" : "Python",
    "framework" : "Flask",
    "website" : "Scotch",
    "version_info" : {
        "python" : 3.4,
        "flask" : 0.12
    },
    "examples" : ["query", "form", "json"],
    "boolean_test" : True
}

data = str.encode(json.dumps(data))

# Com a chave correta
headers = {'Content-type': 'application/json', 'Autorization':'42'}
pg = get(url, data=data, headers=headers)
print('\n',pg.text)

# Com a chave incorreta
headers = {'Content-type': 'application/json', 'Autorization':'12'}
pg = get(url, data=data, headers=headers)
print('\n',pg.text)