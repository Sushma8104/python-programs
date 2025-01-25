#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import download
download('punkt')
download('stopwords')
download('wordnet')
text = """
Natural language processing is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages.
"""
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words and word.isalpha()]  # Remove punctuation
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
print("Original tokens:", tokens)
print("Stemmed tokens:", stemmed_tokens)
print("Lemmatized tokens:", lemmatized_tokens)
dictionary = corpora.Dictionary([lemmatized_tokens])
corpus = [dictionary.doc2bow(lemmatized_tokens)]
tfidf = gensim.models.TfidfModel(corpus)
tfidf_corpus = tfidf[corpus]
for doc in tfidf_corpus:
    print(doc)


# In[ ]:





# In[ ]:




