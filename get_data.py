# %%
import pandas as pd
import numpy as np
import urllib3

# %%
df = pd.DataFrame(columns = ['noticia', 'label'])

# %%
http = urllib3.PoolManager() # PoolManager
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Desabilitando avisos

# %%
for i in range(1, 3601):
  url = "https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/full_texts/fake/%d.txt" % i # URL da notícia
  r = http.request('GET', url) # Copiando notícia
  noticia = pd.DataFrame([[r.data.decode('utf-8'), 'fake']], columns = ['noticia', 'label'])
  df = df.append(noticia, ignore_index=True)

for i in range(1, 3601):
  url = "https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/full_texts/true/%d.txt" % i # URL da notícia
  r = http.request('GET', url) # Copiando notícia
  noticia = pd.DataFrame([[r.data.decode('utf-8'), 'true']], columns = ['noticia', 'label'])
  df = df.append(noticia, ignore_index=True)
  
# %%
df2 = pd.read_csv('https://raw.githubusercontent.com/ViniciusNunes0/SIRENE-news/master/noticias-sirene.csv', sep=';')
df2 = df2[['noticia', 'classificacao']]
df2 = df2.rename(columns={"noticia": "noticia", "classificacao": "label"})
df2['label'] = df2['label'].replace({0: 'true', 1: 'fake'})
df2.head()
df = df.append(df2, ignore_index=True)

# %%
df.to_csv(r"dados/fake_news_data.csv", index = None, header=True)
