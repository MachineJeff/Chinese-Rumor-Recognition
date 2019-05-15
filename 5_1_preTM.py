import json
import os.path
file = "datap/data_1.json"

data = []
with open(file) as fp:
	for line in fp.readlines():
		data.append(json.loads(line))					


file1 = "datap/textList.txt"
file2 = "datap/tagList.txt"

with open(file1,'w') as fp:
	for x in data:
		fp.write(x["text"])
		fp.write('\n')

with open(file2,'w') as fp:
	for x in data:
		temp = str(x["isRumor"])
		fp.write(temp)
		fp.write('\n')





