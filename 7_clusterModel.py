import json
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from time import time

file = "datap/jieba.txt"
corpus = []

with open(file,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		corpus.append(line)

print(len(corpus))


vectorizer=CountVectorizer()

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  

tag = []
tagfile = "datap/tagList.txt"
with open (tagfile,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		if(line == "False"):
			tag.append(0)
		else:
			tag.append(1)

print(tag[:2])


volume = (len(corpus)//3) *2
print(volume)

x_train = tfidf[:volume,]
y_train = tag[:volume]

x_test = tfidf[volume:,]
y_test = tag[volume:]



def count(number):
	t = time()
	kmean = KMeans(n_clusters = number, max_iter = 100, tol = 0.01, verbose = 0, n_init = 9)
	kmean.fit(tfidf)
	print('time cost = {}'.format(time()-t))


	rumorPro = dict()
	norumorPro = dict()

	for i in range(len(tag)):
		if(tag[i] == 1):
			if(rumorPro.__contains__(kmean.labels_[i])):
				rumorPro[kmean.labels_[i]] += 1
			else:
				rumorPro[kmean.labels_[i]] = 1
		else:
			if(norumorPro.__contains__(kmean.labels_[i])):
				norumorPro[kmean.labels_[i]] += 1
			else:
				norumorPro[kmean.labels_[i]] = 1

	pre = []
	for i in range(number):
		y = 0
		p = 0
		if(rumorPro.__contains__(i)):
			y = rumorPro[i]
		if(norumorPro.__contains__(i)):
			p = norumorPro[i]

		temp = y/(y+p)

		if(temp>0.5):
			pre.append(temp)
		else:
			pre.append(1-temp)

	score = sum(pre)/len(pre)
	print('score = {}'.format(score))

	prep = []
	for i in range(number):
		y = 0
		p = 0
		if(rumorPro.__contains__(i)):
			y = rumorPro[i]
		if(norumorPro.__contains__(i)):
			p = norumorPro[i]

		temp = y/(y+p)
		prep.append(temp)

	lable = kmean.labels_
	return (prep,lable)

# for i in range(3,21):
# 	print('This is NO.{} epoch'.format(i))
# 	count(i)
# 	print()

##10类的效果最好

result = count(10)

print(result[0])
print(result[1])

classList = "datap/classList.txt"
scoreList = "datap/scoreList.txt"

with open(classList,"w") as fp:
	for x in result[1]:
		fp.write(str(x))
		fp.write("\n")

with open(scoreList,"w") as fp:
	for x in result[0]:
		fp.write(str(x))
		fp.write("\n")



