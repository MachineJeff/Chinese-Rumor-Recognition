import json

data = []

file1 = "datap/data.json"

with open(file1) as fp:
	for line in fp.readlines():
		data.append(json.loads(line))

features = set()
userfeatures = set()

for x in data:
	for item in x.keys():
		features.add(item)

print(features)
print()

# 删除time，查看multi，删除source，取出user
users = []
mulset = set()
for x in data:
	del x["time"]
	del x["source"]
	users.append(x["user"])
	del x["user"]
	if(x.__contains__("multi")):
		mulset.add(x["multi"])

print(mulset)

userf = set()
for x in users:
	if(type(x) == dict):
		for key in x.keys():
			userf.add(key)
print(userf)


for i in range(len(data)):
	if(type(users[i]) == dict):
		del users[i]["time"]
		del users[i]["location"]
		data[i].update(users[i])

print(len(users))
print(len(data))

newdata = []

for i in range(len(users)):
	if(type(users[i]) == dict):
		newdata.append(data[i])

print(len(newdata))

print(newdata[:2])

file_data = "datap/data_1.json"

with open(file_data,'w') as fp:
	for x in newdata:
		dicc = json.dumps(x,ensure_ascii=False)
		fp.write(dicc)
		fp.write('\n')

