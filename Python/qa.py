#!/usr/bin/python 3
# encoding: utf-8

import os
import math
import operator
import jieba
import codecs
import heapq
import numpy as np
import sys
from sklearn.feature_extraction.text import TfidfVectorizer

def read(path):  # 读取txt文件，并返回list
	f = open(path,encoding="utf-8")
	data = []
	for line in f.readlines():
		#print(line)
		data.append(line)
	f.close()
	return data

def getstopword(path):  # 获取停用词表
	swlis = []
	for i in read(path):
		outsw = str(i).replace('\n', '')
		swlis.append(outsw)
	return swlis
#结巴分词，切开之后，有分隔符
def jieba_function(sent,swlist):
	import jieba
	sent1 = jieba.cut(sent)
	s = []
	for each in sent1:
		if each not in swlist:
			s.append(each)
	return ' '.join(str(i) for i in s)

def count_cos_similarity(vec_1, vec_2):
	if len(vec_1) != len(vec_2):
		return 0

	s = sum(vec_1[i] * vec_2[i] for i in range(len(vec_2)))
	den1 = math.sqrt(sum([pow(number, 2) for number in vec_1]))
	den2 = math.sqrt(sum([pow(number, 2) for number in vec_2]))
	return s / (den1 * den2)

def tfidf(sent1, sent2):

	tfidf_vec = TfidfVectorizer()

	sentences = [sent1, sent2]
	print(tfidf_vec.fit_transform(sentences).toarray())
	print(tfidf_vec.get_feature_names())
	vec_1 = tfidf_vec.fit_transform(sentences).toarray()[0]
	vec_2 = tfidf_vec.fit_transform(sentences).toarray()[1]
	similar=count_cos_similarity(vec_1, vec_2)
	print(similar)

	return similar

def main():
	threshold=0.5 #相似度阈值设定

	question=input("请输入您的问题:")
	swpath = r'C:\Users\bubble sponge\Desktop\Python\停用词表.txt'#停用词表路径
	swlist = getstopword(swpath)  # 获取停用词表列表
	question=jieba_function(question,swlist)

	fctquestion_filepath = r'C:\Users\bubble sponge\Desktop\Python\fctquestion.txt'
	fctquestion_lists = read(fctquestion_filepath)  # 获取所有已分词问题返回为列表
	question_filepath = r'C:\Users\bubble sponge\Desktop\Python\question.txt'
	question_lists = read(question_filepath)   #获取所有未分词问题返回为列表
	simi_lists=[]
	fresult=open(r'C:\Users\bubble sponge\Desktop\Python\tfidf_result.txt','w',encoding='utf-8')
	for q_list in fctquestion_lists:
		tfidf_result=tfidf(question,''.join(q_list))
		simi_lists.append(tfidf_result)
		fresult.write(str(tfidf_result)+'\n')
	fresult.close()
	answer_path=r'C:\Users\bubble sponge\Desktop\Python\answer.txt'
	answer_lists=read(answer_path)#读取问题库对应的答案汇成的列表
	max_index=[]
	
	re1 = list(map(simi_lists.index, heapq.nlargest(5, simi_lists))) #求最大的三个索引
	for i in range(5):
		if simi_lists[re1[i]]<0.5 and i==0:
			print("没有找到您所提出的问题的解决方法")
			return 0
		else:
			print(question_lists[re1[i]]+'\n')
			print(answer_lists[re1[i]]+'\n')
			print(simi_lists[re1[i]]+'\n')
	return 0



if __name__ == '__main__':
	main()
