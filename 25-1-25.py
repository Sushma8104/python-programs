#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text.lower()
input_text = 'HELLO, WORLD! WELCOME TO NLP 101.'
cleaned_text = clean_text(input_text)
print(cleaned_text)


# In[ ]:




