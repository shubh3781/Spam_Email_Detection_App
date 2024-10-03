# Import Lib

from pickle import load
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

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



#load model and vectorize file
fv = open("tv_spam.pkl","rb")
tv=load(fv)
fv.close()

fm = open("model.spam.pkl","rb")
model=load(fm)
fm.close()


txt = input("enter text ")
ctxt = clean_text(txt)
vtxt =tv.transform([ctxt])
res=model.predict(vtxt)
print(res)
