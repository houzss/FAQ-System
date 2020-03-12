#主函数
QTFIDF_PATH='data/1quetTFIDF.txt'
T2_path='data/T2.txt'
out_path='data/simil.txt'
answer_path='data/1answer.txt'
question_path='data/1question.txt'

from perfcty import writewords
from pertfidf import runn,fun,runn1
from TFIDF import write
import heapq

#判断相似度
def judge(PATH,r_no,r_v,QT2):
	cosin=[]
	WT2=fun(T2_path)
	l=0
	f = open(PATH, encoding="UTF-8-sig")
	for line in f:

		no=[]
		v=[]
		sencosin=0
		line=line.lower().strip().split()
		for i in range(len(r_no)):
			for a in line:
				a=a.strip(':').split(':')
				if r_no[i]==a[0]:
					
					sencosin=sencosin+(float(r_v[i])*float(a[1]))
					#print(r_no[i]+' '+a[0]+' '+str(float(r_v[i])*float(a[1]))+' '+str(sencosin))
					break
				#print(float(r_v[i])*float(a[1]))
		sencosin=sencosin/(float(WT2[l])*float(QT2)+1)
		#print(sencosin)
		cosin.append(sencosin)	
		l=l+1
	f.close()
	return cosin

#对问句预处理
def prepare(x):
	#对问题进行分词
	s=writewords(x)

	#print(s)
	#生成向量-不用同义词
	result=runn(s)
	#result=runn1(s)
	r_no=[]
	r_v=[]
	T2=0
	for a in result:
		a=a.strip(':').split(':')
		#print(a)
		r_no.append(a[0])
		r_v.append(a[1])
		b=int(a[1])*int(a[1])
		T2=T2+b  
	T2=T2 ** 0.5 

	return r_no,r_v,T2

def sortt(cosin):
	re2 = heapq.nlargest(5, cosin)
	idff=[]
	idff=fun(out_path)
	nolist=[]
	count=0
	for i in range(len(re2)):
		l=0
		for line in idff:
			a=re2[i]
			a=str(a)
			if a==line:
				nolist.append(l)

				count=count+1
				#print('yeah')
			if count>4:
				break
			l=l+1
		if count>4:
			break
			
	#print(nolist)
	return nolist,re2

def match(x):
	'''
	x=input("请输入您的问题：")
	print(x)
	'''
	

	#导入回答
	answer=[]
	f = open(answer_path, encoding="UTF-8-sig")
	answer=f.read()
	answer=answer.strip('\n').split('\n')
	f.close()
	#导入相似问题
	quesion=[]
	f = open(question_path, encoding="UTF-8-sig")
	quesion=f.read()
	quesion=quesion.strip('\n').split('\n')
	f.close()
	


	#对问题进行处理
	r_no=[]
	r_v=[]
	#x="请问 我为什么不可以交易ST股票了？"
	astring=[]
	(r_no,r_v,QT2)=prepare(x)
	#print(QT2)
	
	cosin=judge(QTFIDF_PATH,r_no,r_v,QT2)
	write(cosin,out_path)
	(no,v)=sortt(cosin)
	simi=[]
	astring=[]
	#print('\n你的问题：'+x)
	for i in range(0,5):
		#print('\n相似度：'+str(v[i])+'\n相似问题：'+quesion[no[i]]+'\n回答：'+answer[no[i]])
		if v[i]>0.5 :
			simi.append(str(v[i]))
			astring.append(str(quesion[no[i]]+'-'+answer[no[i]]))
		#print(simi[i])
		#print(astring[i])
	#print(no)
	if len(simi)==0:
		return -1,-1
	else:
		return simi,astring
	
