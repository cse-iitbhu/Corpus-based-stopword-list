import glob
corpus=[]
files = glob.glob("./marathi/alreadydoneuniq/*.txt")

for fle in files:

    with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
        corpus.append(text)
new=[]
for i in corpus:
    a=str(i)[26:-16]
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' '))
corpus=new
import os
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

import random
import string
from nltk.stem import PorterStemmer
ps = PorterStemmer()
corpus1=[]
for sent in range(len(corpus)-1):
    sent1=[]
    wrds = word_tokenize(corpus[sent])
    for i in range(len(wrds)-1):
        sent1.append(ps.stem(wrds[i]))
    corpus1.append(' '.join(sent1))
lexicon=corpus1
corpus=lexicon

import random
num1 = random.randrange(0, len(corpus)-1)
subcorp = corpus[num1]
words=[]
for word in subcorp:

    words.append(word)
num2 = random.randrange(0, len(words)-1)
wr=words[num2]
lex=[]
for sent in lexicon:
    if wr in sent:
        lex.append(sent)
freq_doc={}
def tf(corpus):

    dic={}
    
    for i in range(len(corpus)):
       
        
        for word in nltk.word_tokenize((corpus[i])):
            
            if word in dic:
                dic[word] = dic[word] + 1
               
            else:
                dic[word]=1
    return dic

new_tf_val=tf(lex)
freq_doc=new_tf_val
most_freq=[k  for  k in new_tf_val.keys()]

freq_doc1={}
def tf1(corpus):

    dic={}
    
    for i in range(len(corpus)):
       
        
        for word in nltk.word_tokenize((corpus[i])):
            
            if word in dic:
                dic[word] = dic[word] + 1
               
            else:
                dic[word]=1
    return dic
s=0
for sent in lex:
    s+=1
word_tf_values=tf1(corpus)
freq_doc1=word_tf_values
tokenc=0
for i in lexicon:
    w=[]
    w=nltk.word_tokenize(i)
    tokenc+=len(' '.join(w))
wt=[]
import math
key=freq_doc.keys()
keys=freq_doc1.keys()
for i in key:
    wt.append((freq_doc[i]/s)*(math.log((freq_doc[i]/s)/(freq_doc1[i]/tokenc))))
wgt=[]
for i in wt:
    wgt.append(i/max(wt))
key=list(key)
stpdi={}
for i in range(len(key)-1):
    stpdi[key[i]]=wgt[i]
import operator

print('Term Based=')
n=500
a3={k: v for k, v in sorted(stpdi.items(), key=lambda item: item[1], reverse=True)}
k3={key:value for key,value in list(a3.items())[0:n]}
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")
