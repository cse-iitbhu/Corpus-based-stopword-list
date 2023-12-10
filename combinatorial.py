
import glob
corpus=[]
#files = glob.glob("./marathi/alreadydoneuniq/*.txt")
files = glob.glob("./Desktop/marathi/alreadydoneuniq/*.txt")
for fle in files:

    with open(fle, encoding="utf8", errors='ignore') as f:
        text = f.read()
        corpus.append(text)
new=[]
for i in corpus:
    a=str(i)[26:-16]
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
corpus=new
import nltk
from nltk import word_tokenize
import os
import numpy as np
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

new_tf_val=tf(corpus)
too_many = {key: value for key, value in new_tf_val.items() if value >= 200}
most_freq=[k  for  k in too_many.keys()]
def nextword(target, source):
     for i, w in enumerate(source):
                if w == target:
                    return source[i+1]
tcf={}
for word in most_freq:
        try:
                a=[]
                count=0
                for i in range(len(corpus)):
                            string=nltk.word_tokenize((corpus[i]))
                            b=nextword(word,string)
                            if b not in a:
                                a.append(b)
                                count=count+1

                tcf[word]=count
        except:
            continue

import statistics
threshold= statistics.median(list(tcf.values()))

tcf_final=dict([(k,v) for k,v in tcf.items() if v >= threshold])
sort_orders = sorted(tcf_final.items(), key=lambda x: x[1], reverse=True)

print('Values=')
n=500
a3={k: v for k, v in sorted(tcf.items(), key=lambda item: item[1], reverse=True)}
k3={key:value for key,value in list(a3.items())[0:n]}
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")

