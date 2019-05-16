import numpy as np
file1 = "datap/tfidfPro.txt"
file2 = "datap/logPro.txt"
file3 = "datap/classList.txt"
file4 = "datap/scoreList.txt"
file5 = "datap/tagList.txt"

tfidf = []
log = []

classlist = []
scorelist = []

tag = []

with open(file1,"r") as fp:
	for line in fp.readlines():
		line = line.strip("\n")
		tfidf.append(line)


with open(file2,"r") as fp:
	for line in fp.readlines():
		line = line.strip("\n")
		log.append(line)


with open(file3,"r") as fp:
	for line in fp.readlines():
		line = line.strip("\n")
		classlist.append(line)

with open(file4,"r") as fp:
	for line in fp.readlines():
		line = line.strip("\n")
		scorelist.append(line)

with open(file5,"r") as fp:
	for line in fp.readlines():
		line = line.strip("\n")
		tag.append(line)
for i in range(len(tag)):
	if(tag[i] == 'False'):
		tag[i] = 0
	else:
		tag[i] = 1

clustepro = []

for i in range(len(classlist)):
	cla = classlist[i]
	clustepro.append(float(scorelist[int(cla)-1]))




volume = (len(tag)//3) *2

# def weight(w1, w2, w3):
# 	newscore = []
# 	for i in range(volume):
# 		temp = w1*float(tfidf[i]) + w2*float(log[i]) + w3*float(clustepro[i])
# 		newscore.append(temp)

# 	truesum = 0
# 	for i in range(volume):
# 		if(newscore[i]<0.5):
# 			newscore[i] = 1
# 		else:
# 			newscore[i] = 0
# 		if(newscore[i] == tag[i]):
# 			truesum += 1

# 	rate = truesum/volume
# 	return rate



# max = 0
# dic = {}

# for i in np.arange(0, 1.01, 0.01):
# 	for j in np.arange(0, 1.01-i, 0.01):
# 		sco = weight(i, j, 1-i-j)
# 		if(sco > max):
# 			max = sco
# 			dic[max] = "{} + {} + {}".format(i, j, 1-i-j)

# ma = 0
# for key in dic.keys():
# 	if(key>ma):
# 		ma = key
# print(ma)
# print(dic[ma])

def weight(w1, w2, w3):
	newscore = []
	for i in range(volume,len(tag)):
		temp = w1*float(tfidf[i]) + w2*float(log[i]) + w3*float(clustepro[i])
		newscore.append(temp)

	truesum = 0
	for i in range(len(newscore)):
		if(newscore[i]<0.3):
			newscore[i] = 1
		else:
			newscore[i] = 0
		if(newscore[i] == tag[volume+i]):
			truesum += 1

	rate = truesum/volume
	return rate

max = 0
dic = {}

for i in np.arange(0, 1.01, 0.01):
	for j in np.arange(0, 1.01-i, 0.01):
		sco = weight(i, j, 1-i-j)
		if(sco > max):
			max = sco
			dic[max] = "{} + {} + {}".format(i, j, 1-i-j)

ma = 0
for key in dic.keys():
	if(key>ma):
		ma = key
print(ma)
print(dic[ma])
