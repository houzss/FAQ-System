
import jieba
stopwords_path='data/1stopwords.txt'



jieba.suggest_freq('中签', True)  
jieba.suggest_freq('深港通', True) 




def tokenizer(s,stopwords):
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords:
            words.append(word)
    return words

def writewords(s):
    # 设置停用词

    stopwords = []
    with open(stopwords_path, 'r',encoding="UTF-8-sig") as f:
        for line in f:
            if len(line)>0:
                stopwords.append(line.strip())
    s=tokenizer(s.strip(),stopwords)
    #print(s)
    return(" ".join(s))


