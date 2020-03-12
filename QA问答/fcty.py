#coding=utf-8
import jieba
 
input_path='data/1question.txt'
output_path='data/fctyquestion.txt'
keyword_path='data/keyword.txt'
stopwords_path='data/1stopwords.txt'

#添加专有名词


jieba.suggest_freq('中签', True)  #0.03
jieba.suggest_freq('深港通', True) #0.03




def tokenizer(s,stopwords):
    words = []
    cut = jieba.cut(s)

    for word in cut:
        if word not in stopwords:
            words.append(word)
    return words

def writewords():
    # 设置停用词
    stopwords = []
    with open(stopwords_path, 'r',encoding="UTF-8-sig") as f:
        for line in f:
            if len(line)>0:
                stopwords.append(line.strip())
#读取文件数据，分词，并输出到文件
    with open(output_path,'w',encoding="UTF-8-sig") as o:
        with open(input_path, 'r',encoding="UTF-8-sig") as f:
            for line in f:
                s=tokenizer(line.strip(),stopwords)
                o.write(" ".join(s)+"\n")

def write(alist,out_path):
    f=open(out_path,'w',encoding="UTF-8-sig")
    for line in alist:
        f.write(str(line)+'\n')
        #print(line)
    f.close()


def getwords():
    a=[]
    with open(output_path, 'r',encoding="UTF-8-sig") as f:
        for line in f:
            line=line.lower().strip().split()
            for word in line:
                if word in a:
                    pass
                else:
                    #if(.count(word)>0):
                    a.append(word)
    write(a,keyword_path)

def run1():
    
    writewords()
    getwords()
    return 1

#run1()