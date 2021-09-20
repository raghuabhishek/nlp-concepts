#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:47:21 2021

@author: abhishekr
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



paragraph="I am Abhishek and playful boy. I am Appa and good boy. I am Amma and good girl."

lemmatizer=WordNetLemmatizer()

#Tokenization
sentences=nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    result=[]
    for word in words:
        if word not in set(stopwords.words('english')):
            result.append(lemmatizer.lemmatize(word))
    sentences[i]=" ".join(result)
            