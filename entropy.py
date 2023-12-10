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
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
corpus=new
import os
import numpy as np
import nltk
from nltk import word_tokenize
def tf(corpus):
    dic={}
    for i in range(len(corpus)):
       
        
        for word in nltk.word_tokenize((corpus[i])):
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word]=1
   
    return dic

new_tf_val=tf(corpus)
too_many = {key: value for key, value in new_tf_val.items() if value >= 200}
most_freq=[k  for  k in too_many.keys()]
def tf1(corpus):
    tfs = []
    for i in range(len(corpus)):
        k=nltk.word_tokenize((corpus[i]))
        dic={}
        for word in k:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
        for word,freq in dic.items():

            dic[word]=freq/len(k)
        tfs.append(dic)
    return tfs
tf_val=tf1(corpus)
p_fin={}
for word in most_freq:

    l=[]
    for i in tf_val:
        if word in list(i.keys()):
            l.append(i[word])
        else:
            l.append(0)
    p_fin[word]=l
import math
w={}
for token in most_freq:
    s=0
    for i in range(len(corpus)):
        x=p_fin[token][i]

        s=s+ ((x)* math.log(1/(x+1)))
    w[token]=s

print('Entropy=')
n=500
a3={k: v for k, v in sorted(w.items(), key=lambda item: item[1], reverse=True)}
k3={key:value for key,value in list(a3.items())[0:n]}
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")
