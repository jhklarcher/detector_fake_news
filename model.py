# %%
# Imports
import nltk
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from lightgbm import LGBMClassifier
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import urllib3
import joblib as jl


# %% 
# Dataframe
df = pd.read_csv('dados/fake_news_data.csv')

# %%
# Train-test split
x_train,x_test,y_train,y_test = train_test_split(df['noticia'],
                                                 df['label'],
                                                 test_size=0.2,
                                                 random_state=0)

# %%
# tf-dif
tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('portuguese'),
                                   analyzer='word',
                                   ngram_range=(1, 1),
                                   lowercase=True,
                                   use_idf=True)

# %%
# Apply to train and test
tfidf_train = tfidf_vectorizer.fit_transform(x_train) 
tfidf_test = tfidf_vectorizer.transform(x_test)

# %%
# Model
model = LGBMClassifier(learning_rate=0.1,
                      num_leaves=128,
                      min_child_samples=100,
                      ubsample=0.96,
                      colsample_bytree=0.28,
                      random_state=0,
                      subsample_freq=1,
                      n_estimators=100)
model.fit(tfidf_train,y_train)

y_pred = model.predict(tfidf_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

# %%
# Saving model
jl.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl.z')
jl.dump(model, 'model.pkl.z')


# %%
