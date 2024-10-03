# Import Lib

import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from pickle import dump

# load the data
data = pd.read_csv("spam.csv")
print(data)

# check for null value
print(data.isnull().sum())

# text cleaning
ps = PorterStemmer()
def clean_text(txt):
	txt = txt.lower()
	txt = word_tokenize(txt)
	txt = [t for t in txt if t not in punctuation ]
	txt = [t for t in txt if t not in stopwords.words('english')]
	txt = [ps.stem(t) for t in txt]
	txt = " ".join(txt)
	return txt


data["clean_text"]=data["Message"].apply(clean_text)
print(data)

# text vectorizer with Tfidf

tv = TfidfVectorizer()
vector = tv.fit_transform(data['clean_text'])


# feature and target
features = pd.DataFrame(vector.toarray(),columns=tv.get_feature_names_out())
target= data['Category']
#print(features)

# train and test
x_train,x_test,y_train,y_test=train_test_split(features.values,target)

#model
model=MultinomialNB()
model.fit(x_train,y_train)

#classification report
cr= classification_report(y_test,model.predict(x_test))
print(cr)


# generating model file
fv = open("tv_spam.pkl","wb")
dump(tv,fv)
fv.close()

fm = open("model.spam.pkl","wb")
dump(model,fm)
fm.close()
