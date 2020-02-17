# %%
# Imports
from newsplease import NewsPlease
import requests
import json

# %%
noticia_url = "https://oglobo.globo.com/sociedade/antartica-registra-temperatura-acima-de-20c-pela-primeira-vez-na-historia-24246734?utm_source=Whatsapp&utm_medium=Social&utm_campaign=compartilhar"
#f = open("noticia_teste.txt", "r", encoding="utf8")
#noticia = f.read() #.encode('utf-8')

# %%
# local url
#url = 'http://127.0.0.1:5000'
url = 'https://detector-fake-news.herokuapp.com'

# %%
# sample data
data = {'url': noticia_url}
data = json.dumps(data)

# %%
send_request = requests.post(url, data)
print(send_request.json())

# %%
