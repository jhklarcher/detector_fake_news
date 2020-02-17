# %%
# Imports
from newsplease import NewsPlease
import requests
import json

# %%
noticia_url = "https://g1.globo.com/mundo/noticia/2020/02/16/cidades-esponja-conheca-iniciativas-pelo-mundo-para-combater-enchentes-em-centros-urbanos.ghtml"
#f = open("noticia_teste.txt", "r", encoding="utf8")
#noticia = f.read() #.encode('utf-8')

# %%
# local url
url = 'http://127.0.0.1:5000'

# %%
# sample data
data = {'url': noticia_url}
data = json.dumps(data)

# %%
send_request = requests.post(url, data).json()
print(send_request)

# %%
