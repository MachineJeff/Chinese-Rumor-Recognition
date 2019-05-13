import json

data = []

file1 = "/home/jeffrey/paper/datap/data.json"

with open(file1) as fp:
	for line in fp.readlines():
		data.append(json.loads(line))

features = set()
userfeatures = set()

for x in data:
	for item in x.keys():
		features.add(item)
	if(x.__contains__('user')):
		if(type(x["user"]) == dict):
			temp = x["user"]
			for key in temp.keys():
				userfeatures.add(key)

print(features)
print(userfeatures) 
print()


##提取一般性特征
fList = ["has_url","pics","multi","commets","reposts","source","likes","gender","location","followers","friends","messages","verified","verified_type","description"]
ffList = ["time","usertime"]##不需要的变量

##先处理verified和verified_type
##查看二者都有什么类别

v = set()
vtype = set()
for x in data:
	if(x.__contains__('user')):
		if(type(x["user"]) == dict):
			temp = x["user"]
			if(temp.__contains__("verified")):
				v.add(temp["verified"])
			if(temp.__contains__("verified_type")):
				vtype.add(temp["verified_type"])

print(v)
print(vtype)
print()


vt = set()
for x in data:
	if(x.__contains__('user')):
		if(type(x["user"]) == dict):
			temp = x["user"]
			if(temp.__contains__("verified")):
				if(temp["verified"] == False):
					vt.add(temp["verified_type"])

print(vt)
print()

##统一verified和verified_type
##并删除两个时间
for x in data:
	if(x.__contains__("time")):
		del x["time"]
	if(x.__contains__("user")):
		if(type(x["user"]) == dict):
			if(x["user"].__contains__("time")):
				del x["user"]["time"]
			if(x["user"].__contains__("verified")):
				if(x["user"]["verified"] == False):
					if(x["user"].__contains__("verified_type")):
						x["user"]["verified_type"] = -1
				del x["user"]["verified"]

print(data[:2])
print()

##把user信息都统一成特征
##空的user数据删除

for x in data:
	if(x.__contains__("user")):
		if(type(x["user"]) != dict):
			data.remove(x)
		else:
			temp = x["user"]
			del x["user"]
			x.update(temp)

print(data[:2])
print()


file_data = "/home/jeffrey/paper/datap/data_1.json"

with open(file_data,'w') as fp:
	for x in data:
		dicc = json.dumps(x,ensure_ascii=False)
		fp.write(dicc)
		fp.write('\n')

