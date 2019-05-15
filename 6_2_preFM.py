import json

file = "datap/data_1.json" 
data = []
with open(file,"r") as fp:
	for line in fp.readlines():
		data.append(json.loads(line))


features = set()

for x in data:
	del x['text']
	del x['verified_type']
	for key in x.keys():
		features.add(key)

print(features)

print(data[:2])


dic = dict()

for x in data:
	for key in x.keys():
		if not (dic.__contains__(key)):
			dic[key] = 1
		else:
			dic[key] += 1

print(dic)
##没有缺失值



##处理multi
mulset = set()
for x in data:
	mulset.add(x["multi"])

print(mulset)


mullist = [None, 'article', 'video', 'topic', 'audio', 'webpage', 'place']

for x in data:
	if(x["multi"] == mullist[0]):
		x["multi"] = 0
	elif(x["multi"] == mullist[1]):
		x["multi"] = 1
	elif(x["multi"] == mullist[2]):
		x["multi"] = 2
	elif(x["multi"] == mullist[3]):
		x["multi"] = 3
	elif(x["multi"] == mullist[4]):
		x["multi"] = 4
	elif(x["multi"] == mullist[5]):
		x["multi"] = 5
	elif(x["multi"] == mullist[6]):
		x["multi"] = 6


##处理has_url
urlset = set()
for x in data:
	urlset.add(x["has_url"])

print(urlset)

urllist = [False,True]

for x in data:
	if(x["has_url"] == urllist[0]):
		x["has_url"] = 0
	else:
		x["has_url"] = 1


##处理verified
verset = set()
for x in data:
	verset.add(x["verified"])

print(verset)

for x in data:
	if(x["verified"] == urllist[0]):
		x["verified"] = 0
	else:
		x["verified"] = 1

##处理gender
genset = set()
for x in data:
	genset.add(x["gender"])

print(genset)

genlist = ['f','m']
for x in data:
	if(x["gender"] == genlist[0]):
		x["gender"] = 0
	else:
		x["gender"] = 1

##处理isRumor

for x in data:
	if(x["isRumor"] == urllist[0]):
		x["isRumor"] = 0
	else:
		x["isRumor"] = 1

##处理description

des = set()
for x in data:
	des.add(x["description"])

print(des)

for x in data:
	if(x["description"] == urllist[0]):
		x["description"] = 0
	else:
		x["description"] = 1


file2 = "datap/data_2.json"

with open(file2,"w") as fp:
	for x in data:
		dicc = json.dumps(x,ensure_ascii=False)
		fp.write(dicc)
		fp.write('\n')

