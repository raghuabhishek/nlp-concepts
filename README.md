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
1. A bag-of-words model, or BoW for short, is a way of extracting features from text for use in modeling, such as with machine learning algorithms.
2. This procedure will convert the textual data of sentences into vectors by counting the number of occurances of the words in a sentence.
3. `from sklearn.feature_extraction.text import CountVectorizer`: I have used CountVectorizer to acheive this task which is a part of the sklearn library.
4. `cv.fit_transform(corpus).toarray()`: This statemnt will calculate the vectors for every sentence and return a matrix containing words as columns and sentences as rows.
5. The disadvantage of BoW is that it offers importance to the words based on their number of occurances which will not be helpful in the case where there may be very important keywords which may occur in less number. 

## Term Frequency - Inverse Document Frequency(TF-IDF)
1. Term Frequncy: Ratio of number of occurances of the word to the number of words in the sentence. 
2. Inverse Document Frequency: Ratio of logarithm of number of sentences to the number of sentences containing the word.
3. TF-IDF: Its the product of term frequency and Inverse Document frequency.
4. `from sklearn.feature_extraction.text import TfidfVectorizer`: TfidfVectorizer class will implement this procedure which is included in sklearn library.
5. `X=tfidf.fit_transform(corpus).toarray()`: This statement will calculate the vectors by multiplying TF and IDF.

