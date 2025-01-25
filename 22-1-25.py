#!/usr/bin/env python
# coding: utf-8

# In[2]:


corpus=[
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be that is the question",
    "The early bind catches the worm"
]
tokenized_corpus=[sentence.lower().split() for sentence in corpus]
print("tokenized corpus")
print(tokenized_corpus)


# In[10]:


from gensim.models import word2vec
model=word2vec.Word2Vec(tokenized_corpus,vector_size=50,window=5,min_count=1,sg=0,epochs=10)
model.save("Word2Vec.model")


# In[12]:


vector=model.wv['dog']
print(vector)


# In[14]:


vector=model.wv['single']
print(vector)
vector=model.wv['lazy']
print(vector)


# In[22]:


similar_words=model.wv.most_similar('quick',topn=5)
print("\nMost Similar words to 'quick':")
for word,similarity in similar_words:
    print(f'{word}: {similarity}')
similar_words=model.wv.most_similar('dog',topn=5)
print("\nMost Similar words to 'dog':")
for word,similarity in similar_words:
    print(f'{word}: {similarity}')


# In[53]:


print("I am a good girl")
print("i am a good \ngirl")
print("something \nis better than \rnothing")
print("something \nis better than \tnothing")


# In[56]:


import re
pattern=r'\d+'
string="007 james bond eants to escape npl class"
matching=re.match(pattern,string)
matching.group()


# In[ ]:




