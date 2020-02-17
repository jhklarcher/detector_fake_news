# %%
# Imports
from newsplease import NewsPlease
import requests
import json

# %%
noticia_url = "https://www1.folha.uol.com.br/poder/2020/02/bolsonaro-dribla-conviccoes-e-usa-tom-eleitoral-para-afastar-pressao-apos-morte-de-miliciano.shtml"
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
