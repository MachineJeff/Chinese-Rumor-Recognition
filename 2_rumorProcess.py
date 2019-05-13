import json
import os
import os.path

filter = ['.json']		##设置过滤后缀
location = "/home/jeffrey/paper/data/Chinese_Rumor_Dataset/CED_Dataset/original-microblog"

data = []

files = os.listdir(location)
for file in files:
	ext = os.path.splitext(file)[1]
	if ext in filter:
		apath = os.path.join(location,file)
		try:
			with open(apath) as f:
				dic = json.load(f)
				data.append(dic)
		except:
			print("Something Wrong!")

##查看所有特征
features = set()
for x in data:
	for key in x.keys():
		features.add(key)

print("所有特征如下：")
print(features)
print()



##发现multi和multi_type应该是同一种特征
##下面是验证代码
nMulti=0
nMulti_type=0

print("数据总量 = %d"%len(data))

for x in data:
	if(x.__contains__("multi")):
		nMulti+=1
	if(x.__contains__("multi_type")):
		nMulti_type+=1
print("nMulti = %d, nMulti_type = %d"%(nMulti,nMulti_type))
print("nMulti + nMulti_type == 数据总量？{}".format(nMulti + nMulti_type == len(data)))
print()

##证实了猜想，multi和multi_type的确为同一种特征



##接下来在data中统一他们
for x in data:
	if(x.__contains__("multi_type")):
		tempvalue = x["multi_type"]
		del x["multi_type"]
		x["multi"] = tempvalue




##查看user的所有特征

featureUser = set()
for x in data:
	if(x.__contains__("user")):
		user = x["user"]
		try:
			for key in user.keys():
				featureUser.add(key)
		except:
			pass
##发现并不是每条数据都有user信息，没有的都是empty
print("所有user特征如下：")
print(featureUser)
print()



##保存处理好的data

savedir = "/home/jeffrey/paper/datap"

file1 = "data.json"

with open(os.path.join(savedir,file1),'w') as fp:
	for x in data:
		dicc = json.dumps(x,ensure_ascii=False)
		fp.write(dicc)
		fp.write('\n')
