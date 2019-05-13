import json
import os.path
file = "/home/jeffrey/paper/datap/data_1.json"

data = []
with open(file) as fp:
	for line in fp.readlines():
		data.append(json.loads(line))					

savedir = "/home/jeffrey/paper/datap"
file1 = "textList.txt"
file2 = "tagList.txt"

with open(os.path.join(savedir,file1),'w') as fp:
	for x in data:
		fp.write(x["text"])
		fp.write('\n')

with open(os.path.join(savedir,file2),'w') as fp:
	for x in data:
		temp = str(x["isRumor"])
		fp.write(temp)
		fp.write('\n')





