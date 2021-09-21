# nlp-concepts
This repository contains implementations of all preprocessing that are required to analyze textual information.

The pre-processing steps that are involved are:
1. **Tokenization**
2. **Stemming**
3. **Lemmatization**
4. **Bag of Words(BOW)**
5. Term Frequency-Inverse Document Frequency(TF-IDF) 

##Tokenization
1. The tokenization is a process of breadking down a paragraph/corpus into a set of sentences/documents and words. 
2. I have used nltk library to implement this procedure
3. `nltk.sent_tokenize(paragraph)` is a function which breaks down a paragraph into a list of sentences and returns the list.
4. `nltk.word_tokenize(paragraph)` is a function which breaks down a paragraph into a list of words and returns the list.
