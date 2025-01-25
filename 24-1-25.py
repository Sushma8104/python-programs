#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
text = """
Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language.
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both valuable and meaningful.
"""
sentences = sent_tokenize(text)
print("Sentences:")
for sentence in sentences:
    print(sentence)
print("\n" + "-"*50 + "\n")
words = word_tokenize(text)
print("Words:")
print(words)


# In[ ]:




