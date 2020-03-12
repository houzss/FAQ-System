from gensim.models import word2vec
import logging
path = 'data/fctyquestion.txt'


model2 = word2vec.Word2Vec.load('cd.model')

for key in model2.similar_by_word(u'B股', topn=10):
    print(key[0], key[1])
print('------')
sim3 = model2.most_similar(u'B股', topn=10)
for key in sim3:
    print(key[0], key[1])
print('------')    
sim3 = model2.most_similar(u'B股', topn=20)
print(u'和 B股 与相关的词有：\n')
for key in sim3:
    print(key[0], key[1])
'''
 
##训练word2vec模型
 
# 获取日志信息
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
 
# 加载分词后的文本，使用的是Text8Corpus类
 
sentences = word2vec.Text8Corpus(path)
 
# 训练模型，部分参数如下
model = word2vec.Word2Vec(sentences, size=100, hs=1, min_count=1, window=3)
 
# 模型的预测
print('-----------------分割线----------------------------')
 
# 计算两个词向量的相似度
try:
    sim1 = model.similarity(u'冻结', u'银行')
    sim2 = model.similarity(u'交易', u'证券')
except KeyError:
    sim1 = 0
    sim2 = 0
print(u'相似度为 ', sim1)
print(u'相似度为 ', sim2)
 
print('-----------------分割线---------------------------')
# 与某个词最相的3个字的词
print(u'与A股卡最相近的3个字的词')
req_count = 5
for key in model.similar_by_word(u'银行卡', topn=100):
    if len(key[0]) == 3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break
 
print('-----------------分割线---------------------------')
# 计算某个词的相关列表
try:
    sim3 = model.most_similar(u'银行卡', topn=20)
    print(u'和 银行卡 与相关的词有：\n')
    for key in sim3:
        print(key[0], key[1])
except:
    print(' error')
 
print('-----------------分割线---------------------------')
# 找出不同类的词
sim4 = model.doesnt_match(u'银行卡 证券 新三板 交易'.split())
print(u'银行卡 证券 新三板 交易')
print(u'上述中不同类的名词', sim4)
 
print('-----------------分割线---------------------------')
# 保留模型，方便重用
model.save(u'cd.model')
 
# 对应的加载方式
# model2 = word2vec.Word2Vec.load('搜狗新闻.model')
# 以一种c语言可以解析的形式存储词向量
# model.save_word2vec_format(u"书评.model.bin", binary=True)
# 对应的加载方式
# model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)
 
 
'''