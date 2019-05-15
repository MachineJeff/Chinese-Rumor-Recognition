import numpy as np
import json
from sklearn.linear_model import LogisticRegression

file = "datap/data_2.json" 
data = []
with open(file,"r") as fp:
	for line in fp.readlines():
		data.append(json.loads(line))


features = set()

for x in data:
	for key in x.keys():
		features.add(key)


##提取所有数据


keylist = list(features)
keylist.remove("isRumor")
print(keylist)

array = []
tag = []

for x in data:
	temp = []
	for key in keylist:
		temp.append(x[key])
	array.append(temp)
	tag.append(x["isRumor"])

print(array[:3])
print(tag[:3])

##建模
# matrix = np.mat(array)
volume = (len(array)//3) *2

x_train = array[:volume]
y_train = tag[:volume]

x_test = array[volume:]
y_test = tag[volume:]

model = LogisticRegression(solver='liblinear')
model.fit(x_train,y_train)
train_score = model.score(x_train,y_train)
test_score = model.score(x_test,y_test)

print('train_score:{}'.format(train_score))
print('test_score:{}'.format(test_score))
