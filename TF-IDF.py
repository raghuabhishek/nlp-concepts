#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:32:32 2021

@author: abhishekr
"""
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

paragraph="I am Abhishek and playful boy. I am Appa and good boy. I am Amma and good girl."

sentences=nltk.sent_tokenize(paragraph)

lemmatizer=WordNetLemmatizer()
corpus=[]
for i in range(len(sentences)):
    review=sentences[i].lower()
    review=re.sub('[^a-zA-Z]',' ',review)
    words=nltk.word_tokenize(review)
    result=[]
    for word in words:
        if word not in set(stopwords.words('english')):
            result.append(lemmatizer.lemmatize(word))
    
    result=" ".join(result)
    corpus.append(result)
    
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer()
X=tfidf.fit_transform(corpus).toarray()