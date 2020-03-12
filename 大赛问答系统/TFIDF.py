filepath='data/fctyquestion.txt'
wordpath='data/keyword.txt'
CiPin_path='data/CIPIN.txt'
WenDangPin_path='data/PERSENT.txt'
TFIDF_path='data/TFIDF.txt'
wenTFIDF_path='data/1quetTFIDF.txt'
T2_path='data/T2.txt'

import math
# 遍历文件夹中的所有文件，返回文件list
def fun(filepath):  
    f = open(filepath, encoding="UTF-8-sig")
    data = []
    for line in f:
        line=line.lower().strip().split()
        data.extend(line)
        #print (line)
    f.close()
    return data
#计算词频
def sum(data,words):
  
    count = []
    for a in words:
        
        count.append(data.count(a))
        
    return count
#计算逆文档频率
def persum(filepath,words):
    count=[]
    
    for a in words:
        f = open(filepath, encoding="UTF-8-sig")
        s=0
        for line in f:
            line = line.lower().strip().split()
            if a in line:
                s=s+1
        count.append(s)
        
    
    return count
#计算一个字词的tfidf值
def tfidf(pre,perpre):
    idf=[]
    tf=pre
    tfidf=[]
    tf=pre
    for i in range(len(perpre)):
        idf.append(math.log10(1318/(int(perpre[i])+1)))
        a=(idf[i]*1.2)*(float(tf[i])**0.2)
        tfidf.append(int(a))
    #print(tfidf)   
    return tfidf
#写入
def write(alist,out_path):
    f=open(out_path,'w')
    for line in alist:
        f.write(str(line)+'\n')
        #print(line)
    f.close()

#给句子生成向量
def runn(tfidf,wen,keyword):
    o=open(wenTFIDF_path,'w')
    
    f = open(filepath, encoding="UTF-8-sig")
    #countline=0
    for line in f:
        
        result=[]
        line = line.lower().strip().split()
        #print(line)  
        #count=0  
        for a in line:
            #print(a)
            #c=line.count(a)/len(line)
            for i in range(len(keyword)):
                if a==keyword[i]:
                    #c=float(tfidf[i])*c
                    result.append(str(i)+":"+str(tfidf[i]))
                    break


        o.write(" ".join(result)+'\n')

        
        #print(result)
    f.close()
    o.close()
                    
#计算分母T平方的开方
def ET2(PATH):
    result=[]
    r = open(PATH, encoding="UTF-8-sig")
    for line in r:  
        
        line = line.lower().strip().split()
        T2=0
        for a in line:
            V=a.strip(':').split(':')
            b=float(V[1])*float(V[1])
            T2=T2+b 
        T2=T2 ** 0.5  
        result.append(T2)
        #print(T2)
    r.close()
    return result









def run2():
    #1
    data=fun(filepath)
    words=fun(wordpath)
    pre=sum(data,words)#词频
    write(pre,CiPin_path)

    perpre=persum(filepath,words)
    write(perpre,WenDangPin_path)
    '''


    '''
    #2

    TFIDF=tfidf(pre,perpre)
    write(TFIDF,TFIDF_path)
    '''

    '''
    #3
    keyword=fun(wordpath)
    wen=fun(filepath)
    result=runn(TFIDF,wen,keyword)
    #print(result)


    #4
    ET2(wenTFIDF_path)
    write(ET2(wenTFIDF_path),T2_path)
    return 1


#run2()