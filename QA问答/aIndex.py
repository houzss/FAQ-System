fctyquestion_path='data/fctyquestion.txt'
question_path='data/1question.txt'
answer_path='data/1answer.txt'



def addQA(Q,A):
	try:
		with open(question_path, 'a+',encoding="UTF-8-sig") as f:
			f.write('\n'+Q)
		with open(answer_path, 'a+',encoding="UTF-8-sig") as o:
			o.write('\n'+A)
		return 1
	except FileNotFoundError:
		return 0



def indexOnce(word,path):
	no=[]
	i=0
	with open(path, 'r',encoding="UTF-8-sig") as f:
		for line in f:
			line=line.lower().strip().split()
			if word in line:
				no.append(i)
			i+=1
	return no

def indexMore(no,word,path):
	no2=[]
	i=0
	with open(path, 'r',encoding="UTF-8-sig") as f:
		for line in f:
			line=line.lower().strip().split()
			if i in no:
				if word in line:
					no2.append(i)
			i+=1
	return no2




def readindex(no,path):
	i=0
	with open(path, 'r',encoding="UTF-8-sig") as f:
		for line in f:
			if i in no:
				print("序号："+str(i)+" 问题:"+line)
			i+=1

def write(alist,out_path):
    f=open(out_path,'w',encoding="UTF-8-sig")
    for line in alist:
        f.write(str(line))
        #print(line)
    f.close()


def deleteq(no,qpath,apath):
	question=[]
	answer=[]
	no=int(no)
	with open(qpath, 'r',encoding="UTF-8-sig") as f:
		i=0
		for line in f:
			if i != no:
				question.append(line)
			i+=1
	with open(apath, 'r',encoding="UTF-8-sig") as f:
		i=0
		for line in f:
			if i != no:
				answer.append(line)
			i+=1
	write(question,question_path)
	write(answer,answer_path)
	print("删除成功")


def mainofindex():
	
	x=input("请输入您的关键词：")

	flag=0
	no=indexOnce(x,fctyquestion_path)
	if(len(no)<1):
		print("找不到关键词,请重新输入\n")
		x=input("请输入您的关键词：")
	else:
		readindex(no,question_path)

	while flag==0:


		s=input("请输入你要操作问题的序号，深入查找请输入*,退出请输入#\n")
		
		if s=='#':
			break
		else:
			if s=='*':
				s=input("请输入关键词:")
				no2=indexMore(no,s,fctyquestion_path)
				if(len(no2)<1):
					print("找不到关键词,请重新输入\n")
					continue
				readindex(no2,question_path)
				no=no2

			else:
				op=input("删除请输入1,退出请输入0\n")
				if op=='1':					
					deleteq(s,question_path,answer_path)
				else :
					break
				#flag=1


#addQA(question_path,answer_path)
#mainofindex()