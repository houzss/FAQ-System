t_question='data/tquestion.txt'
t_answer='data/tanswer.txt'
from qmatch import match
def test():
	f = open(t_question, encoding="UTF-8-sig")

	i=0
	quesion=[]

	o = open(t_answer, encoding="UTF-8-sig")
	quesion=o.read()
	quesion=quesion.strip('\n').split('\n')
	o.close()
	right=0
	for line in f:
		x=line
		(simi,s)=match(x)
		#print(s)
		if s==quesion[i]:
			right=right+1

			'''
			print(simi)
			print(s)
			print(quesion[i])
			'''
		else:

			'''
			print(simi)
			print(s)
			print(quesion[i])
			'''
			
		i=i+1
	print(i)
	print(right)
	print(right/i)
	f.close()

test()