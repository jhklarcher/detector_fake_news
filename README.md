# Detector de fake news
 Criação de um modelo para detecção de noticias falsas em português.
 
 Site:
 
 https://jhklarcher.github.io/projects/detector_fake_news/
 
# Dados

As bases de dados utilizadas foram [SIRENE-news](https://github.com/ViniciusNunes0/SIRENE-news) e [Fake.br-Corpus](https://github.com/roneysco/Fake.br-Corpus).

## Agregação de dados

Com o script `get_data.py` os dados são agregados em um dataframe no pandas, com classificações `true` ou `false` e um [arquivo csv](https://github.com/jhklarcher/detector_fake_news/blob/master/dados/fake_news_data.csv) é criado.

# Modelo

Um modelo é criado e descrito nesse [notebook](https://nbviewer.jupyter.org/gist/jhklarcher/4376f54c01e6d7b8ca3b488f3a24354d). É utilizado uma vetorização Tf–idf nos textos das notícias e um modelo [LightGBM](https://lightgbm.readthedocs.io/en/latest/). Os hiperparâmetros são tunados utilizando o [scikit-optimize](https://scikit-optimize.github.io/auto_examples/index.html) utilizando a função [desse tutorial (muito bom!) do Mario Filho](https://www.youtube.com/watch?v=WhnkeasZNHI).

Os modelos de vetorização e de machinelearning foram salvos em arquivos `.pkl` utilizando a biblioteca [Joblib](https://joblib.readthedocs.io/en/latest/).

# API

Uma API foi criada utilizando Flask no Heroku. A API recebe um request em Json no formato `{url: url_da_noticia}` e retorna um Json no formato:
```
{results: 
{resultado: (true/fake)
, probabilidade: (float)
}
```
O `resultado` indica se a notícia foi considerada verdadeira ou falsa para o modelo e `probabilidade` é a probabilidade de que a notícia seja falsa.

A api pode ser acessada no endereço https://detector-fake-news.herokuapp.com/, que retorna resultados através de requests de aplicativos.

# Página

Foi criada uma [página](https://jhklarcher.github.io/projects/detector_fake_news/) que recebe uma URL de notícia e envia à API, recebendo seu resultado e enviando apresentando de forma mais amigável utilizando JavaScript.
