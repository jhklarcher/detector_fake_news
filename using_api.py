# %%
# Imports
import requests
import json

# %%
# URL da notícia
noticia_url = "https://oglobo.globo.com/sociedade/antartica-registra-temperatura-acima-de-20c-pela-primeira-vez-na-historia-24246734?utm_source=Whatsapp&utm_medium=Social&utm_campaign=compartilhar"


# %%
#  url da API
url = 'https://detector-fake-news.herokuapp.com'

# %%
# deixa na formatação da api
data = {'url': noticia_url}
data = json.dumps(data)

# %%
# envia request e escreve o resultado
send_request = requests.post(url, data)
print(send_request.json())
