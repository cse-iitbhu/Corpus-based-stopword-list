import glob
corpus=[]
files = glob.glob("./Desktop/marathi/alreadydoneuniq/*.txt")


for fle in files:

    with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
        corpus.append(text)
new=[]
for i in corpus:
    a=str(i)[26:-16]
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
corpus=new
import os
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np
l=len(corpus)
def idf(corpus):
    dic={}
    
    
    s={}
    for i in range(len(corpus)):
        
        
        for word in nltk.word_tokenize((corpus[i])):
            
            if word in dic and i != s[word]:
                dic[word] = dic[word] + 1
                s[word]=i
            elif word not in dic:
                dic[word]=1
                s[word]=i
            else:
                continue
           
    for word,freq in dic.items():


        dic[word]=np.log(l/(freq))

    return dic
word_idf_values=idf(corpus)
print('Idf=')
n=500
a3={k: v for k, v in sorted(word_idf_values.items(), key=lambda item: item[1])}
k3={key:value for key,value in list(a3.items())[0:n]}
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")
