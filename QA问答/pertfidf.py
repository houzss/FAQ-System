
wordpath='data/keyword.txt'
wordpath1='data/keywordplus.txt'
TFIDF_path='data/TFIDF.txt'

import math

def fun(filepath):  # 遍历文件夹中的所有文件，返回文件list
    f = open(filepath, encoding="UTF-8-sig")
    data = []
    for line in f:
        line=line.lower().strip().split()
        data.extend(line)
        #print (line)
    return data

def fun1(filepath):  # 遍历文件夹中的所有文件，返回文件list
    f = open(filepath, encoding="UTF-8-sig")
    data = []
    for line in f:
        line=line.lower().strip('\n').split('\n')
        data.extend(line)
        #print (line)
    #print(data[1])
    return data

#给句子生成向量(不用同义词)
def runn(wen):
    keyword=fun(wordpath)
    tfidf=fun(TFIDF_path)
    result=[]
    wen=wen.lower().strip().split()
    for a in wen:
        for i in range(len(keyword)):
            if a==keyword[i]:
                result.append(str(i)+":"+tfidf[i])
                break
        
    return result

#给句子生成向量(用同义词)
def runn1(wen):
    keyword=fun1(wordpath1)
    tfidf=fun(TFIDF_path)
    result=[]
    wen=wen.lower().strip().split()
    for a in wen:

        for i in range(len(keyword)):

            if a in keyword[i]:
                #print("关键字："+a+"\n同义词："+keyword[i])
                #c=line.count(a)/len(line)
                #c=float(tfidf[i])*c
                result.append(str(i)+":"+tfidf[i])
                break
        
    return result

#计算分母T平方的开方          
def ET2(wen):
    result=[]
        
    wen = wen.lower().strip().split()
    T2=0
    for a in wen:
        V=a.strip(':').split(':')
        b=int(V[1])*int(V[1])
        T2=T2+b  
    T2=T2 ** 0.5  
    result.append(T2)
    #print(T2)
    r.close()
    return result


