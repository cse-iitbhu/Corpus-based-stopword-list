
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
    new.append(a.replace('\n', ' ').replace('\u200c', ' ').replace('>', '').replace('HEAD', '').replace('<', '').replace('/', '').replace('HEAD', '').replace('BODY', '').replace('\xa0', '').replace('DOC', '').replace('\u200d', ' ').replace('-', ' ').replace(',', ' ').replace(':', ' ').replace('.', ' ').replace('\'', ' ').replace('|', ' ').replace('(',' ').replace(')', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace('.', ' ').replace('।', ' ').replace('-', ' ').replace('|', ' '))
corpus=new
import os
import numpy as np
freq_doc={}
def ntf(corpus):
    dic={}
    
    s=0
    for i in range(len(corpus)):
       
        
        for word in nltk.word_tokenize((corpus[i])):
            
            if word in dic:
                dic[word] = dic[word] + 1
                s+=1
            else:
                dic[word]=1
                s+=1
            
    for word,freq in dic.items():

    
        dic[word]=-np.log(freq/s)
    return dic

new_tf_val=ntf(corpus)
print('Normalised Tf=')
n=500
a3={k: v for k, v in sorted(new_tf_val.items(), key=lambda item: item[1])}
k3={key:value for key,value in list(a3.items())[0:n]}
print("{" + "\n".join("{!r},".format(k) for k,v in k3.items()) + "}")
