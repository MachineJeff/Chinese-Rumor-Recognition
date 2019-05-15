import re
import json
import jieba
from time import time
from sklearn.feature_extraction.text import TfidfVectorizer
t = time()

file = "datap/textList.txt"
stopword = "datap/stop_word.txt"

##1 读取原始文本数据
data = []
with open(file,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		data.append(line)

##2 载入停用词表
stop = []
with open(stopword,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		line = line.strip()
		stop.append(line)

##3 jieba分词
corpus = []
for i in range(len(data)):
	seg_list = jieba.cut(data[i],)
	temp = ""
	for word in seg_list:
		if word not in stop:
			temp += word
			temp += " "
	temp = temp.strip()				##删除首尾空格
	temp = re.sub(' +', ' ', temp)	##合并多个空格为一个
	corpus.append(temp)

print(corpus[:3])
print(stop[:3])
print(time()-t)


save_jieba = "datap/jieba.txt"

with open(save_jieba,"w") as fp:
	for x in corpus:
		fp.write(x)
		fp.write("\n")
