wordpath='data/keyword.txt'
newwordpath='data/keywordplus.txt'

import synonyms
from TFIDF import write

def sameword():
	
	w = open(newwordpath,'w', encoding="UTF-8-sig")
	f = open(wordpath, encoding="UTF-8-sig")
	for line in f:
		z=0
		i=[]

		#print(line)
		#print(synonyms.nearby(str(line))[0])
		for a in (synonyms.nearby(str(line))[0]):
			#print(a)
			z=z+1
			if a!=[]:
				i.append(a)
			
			if z>2:
				break
		if z==0:
			i.append(line.strip('\n'))
		#print(str(i))
		w.write(" ".join(i)+'\n')
		
	f.close()
	w.close()


sameword()


