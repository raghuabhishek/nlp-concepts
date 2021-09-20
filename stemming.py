#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:09:20 2021

@author: abhishekr
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph="I am Abhishek and playful boy. I am Appa and good boy. I am Amma and good girl." 


sentences=nltk.sent_tokenize(paragraph)

stemmer=PorterStemmer()

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    newwords=[]
    for word in words:
        if word not in set(stopwords.words('english')):
            newwords.append(stemmer.stem(word))
    sentences[i]=" ".join(newwords)
    
print(sentences)


