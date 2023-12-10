#tf
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
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
corpus=new
import os
import numpy as np
#generating term frequencies
freq_doc={}
def tf(corpus):
    dic={}
    #for document in corpus:
    #    for word in document.split():
    #        if word in dic:
    #            dic[word] = dic[word] + 1
    #        else:
    #            dic[word]=1
    for i in range(len(corpus)):
       
        
        for word in nltk.word_tokenize((corpus[i])):
            
            if word in dic:
                dic[word] = dic[word] + 1
               
            else:
                dic[word]=1
                
            
    #for word,freq in dic.items():

    #    freq_doc[word]=freq
    #    dic[word]=freq/sum(map(len, (document.split() for document in corpus)))
    return dic

new_tf_val=tf(corpus)
print('Tf=')
n=500
a3={k: v for k, v in sorted(new_tf_val.items(), key=lambda item: item[1], reverse=True)}
k3={key:value for key,value in list(a3.items())[0:n]}
#print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in k3.items()) + "}")
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")
