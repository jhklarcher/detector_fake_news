import pandas as pd
from flask import Flask, jsonify, request
import joblib as jl
from newsplease import NewsPlease

# load model
model = jl.load('model.pkl.z')
tfidf_vectorizer = jl.load('tfidf_vectorizer.pkl.z')
# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)
    
    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data = pd.DataFrame.from_dict(data)
    
    article = NewsPlease.from_url(str(data.iloc[0,0]))
    noticia = article.maintext
    noticia = pd.DataFrame(data={'noticia':[noticia]})
    print(noticia)
    data_df = tfidf_vectorizer.transform(noticia['noticia'])
    
    # predictions
    result = model.predict(data_df)
    prob = model.predict_proba(data_df)

    # send back to browser
    output = {'resultado': str(result[0]),
              'probabilidade': float(prob[0][0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run()