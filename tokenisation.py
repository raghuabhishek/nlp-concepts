#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:45:01 2021

@author: abhishekr
"""

import nltk
nltk.download()


paragraph="I am Abhishek and good boy. I am Appa and good boy. I am Amma and good girl."


sentences=nltk.sent_tokenize(paragraph)

words=nltk.word_tokenize(paragraph)

print(words)

