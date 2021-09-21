# NLP-concepts
This repository contains implementations of natural language processing techniques using Python programming language.

The pre-processing steps that are involved are:
1. **Tokenization**
2. **Stemming**
3. **Lemmatization**
4. **Bag of Words(BOW)**
5. **Term Frequency-Inverse Document Frequency(TF-IDF)**

## Tokenization
1. The tokenization is a process of breadking down a paragraph/corpus into a set of sentences/documents and words. 
2. I have used nltk library to implement this procedure
3. `nltk.sent_tokenize(paragraph)` is a function which breaks down a paragraph into a list of sentences and returns the list.
4. `nltk.word_tokenize(paragraph)` is a function which breaks down a paragraph into a list of words and returns the list.

## Stemming
1. Stemming is a process of converting the word into its word stem.
2. In Stemming algorithm, the common affixes will be removed from the word to get the root of the word based on fixed rules. Example: > historical => histori
4. The common algorithms in stemming are Porter, Lancaster, etc. I have used Porter Stemming algorithm in my code.
5. The disadvantage of stemming is it may result in overstemming (When it removes the part of the word more than the required) or understemming ( When it removes less part of the word than required).
6. `from nltk.stem import PorterStemmer`: The nltk.stem library contains the class PorterStemmer which can be used for stemming.
7. `stemmer=PorterStemmer()`: An instance of the PorterStemmer class needs to be created to invoke the functions under it.
8. `stemmer.stem(word)`:  This method returns the stemmed word.

## Lemmatization
1. Lemmatization is a process of converting the word into its root/dictionary form.
2. In lemmatization, the word will be reduced to its root form based on the parts of speech of that word. Example: historical => history.
3. I have used WordNet lemmatizer which has a collection of english words in different parts of speech.
4. `from nltk.stem import WordNetLemmatizer`: The nltk.stem library is used that has a WordNetLemmatizer class whose functions can be leveraged.
5. `lemmatizer=WordNetLemmatizer()`: The lemmatizer object is created by instatiating the WordNetLemmatizer class.
6. `lemmatizer.lemmatize(word)`: This method returns the root of the word.

## Bag of Words

