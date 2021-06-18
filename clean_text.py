#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
These functions will achieve corpus-specific text cleaning

@author: Viktoria
April 2021

"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import re


#First lemmatize the text.
def lemmatize(content_as_words):
    
    lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(word):
        #Map POS tag to first character lemmatize() accepts
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    lemma = []
    subset = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in content_as_words]
    #sentence = ' '.join(subset)
    lemma.extend(subset)
    
    return lemma


#Now apply a general text cleaning function that considers the specific properties of the corpus, 
#ie. corpus-sepcific stop words, etc. 

#Takes a string and returns a list with the filtered, lemmatized words.
def clean_text(content, useless, informative):
    
    if content is not None and content != '':
    
        #initial text cleaning
        if type(content) == bytes:
            content = content.decode("utf-8") 
        content = re.findall(r'[a-zA-Z]+', content)
        content = [c.lower() for c in content]
        
        #lemmatize. this will return a list of 1 item: the lemmatized text as a string
        lemma = lemmatize(content)
    
        #treat non-English words and stop words
        en_words = set(nltk.corpus.words.words())
        stop_words = [s for s in stopwords.words('english') if s not in informative]
        
        #get rid of the whole thing if not in English (ratio of en_words is < 40%)
        num_words = len(content)
        content = [c for c in content if c in en_words or c in informative]
        
        #get rid of everything if there aren't enough English words in it
        if num_words == 0 or len(content)/num_words < 0.4:
            content = []
        else:
            #remove stop words
            content = [c for c in content if c not in stop_words and c not in useless]
            #remove short words
            content = [c for c in content if len(c)>=3]
            
    else: 
        content = []
        
    return content