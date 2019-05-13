import json
import os
import os.path


filter = ['.json']		##设置过滤后缀

location = "/home/jeffrey/paper/data/Chinese_Rumor_Dataset/CED_Dataset/original-microblog"
locationrm = "/home/jeffrey/paper/data/Chinese_Rumor_Dataset/CED_Dataset/rumor-repost"
locationnrm = "/home/jeffrey/paper/data/Chinese_Rumor_Dataset/CED_Dataset/non-rumor-repost"

files = os.listdir(location)
filerm = os.listdir(locationrm)
filenrm = os.listdir(locationnrm)

totalfiles = []
rmfiles = []
nrmfiles = []

for file in files:
	ext = os.path.splitext(file)[1]
	if ext in filter:
		totalfiles.append(file)		

for file in filerm:
	ext = os.path.splitext(file)[1]
	if ext in filter:
		rmfiles.append(file)		

for file in filenrm:
	ext = os.path.splitext(file)[1]
	if ext in filter:
		nrmfiles.append(file)		


for item in totalfiles:
	apath = os.path.join(location,item)
	origindata = {}
	with open(apath,'r') as fp:
		s = fp.read()
		data = json.loads(s)
		origindata.update(data)
	
	if item in rmfiles:
		dic = {"isRumor":True}
		origindata.update(dic)
		with open(apath,'w') as fp:
			json.dump(origindata,fp,ensure_ascii=False)
	if item in nrmfiles:
		dic = {"isRumor":False}
		origindata.update(dic)
		with open(apath,'w') as fp:
			json.dump(origindata,fp,ensure_ascii=False)




