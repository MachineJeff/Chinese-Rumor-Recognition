import json

##1读取json文件
location = 'Chinese_Rumor_Dataset/rumors_v170613.json'
data = []
with open(location) as file:
	for line in file.readlines():
		data.append(json.loads(line))



##2查看是否每条数据都有rumorText，publishTime，visitTimes

##这里是一个编程技巧，可以节约时间
tagText = 0
tagPublish = 0
tagVisit = 0
features = set()

for x in data:
	for key in x.keys():
		features.add(key)
	if(tagPublish == 0):
		if(x.__contains__('publishTime') == False):
			tagPublish = 1
	if(tagText == 0):
		if(x.__contains__('rumorText') == False):
			tagText = 1		
	if(tagVisit == 0):
		if(x.__contains__('visitTimes') == False):
			tagVisit = 1

	if(tagPublish+tagText+tagVisit == 3):
		break
print("tagText    = %d"%tagText)
print("tagPublish = %d"%tagPublish)
print("tagVisit   = %d"%tagVisit)
print()
print("all features:")
print(features)
print("number of features:{}".format(len(features)))
print()
##得知不是每条数据都有publishTime，visitTimes
##但是每条数据都有rumorText



##3删除一些不必要的特征

nofeature = ["informerUrl","title","rumormongerName","rumorCode","rumormongerUrl","informerName"]

for x in data:
	for feature in nofeature:
		del x[feature]

print(data[:1])
print()


##4查看多少条信息没有visitTimes,result,publishTime

novisitTimes = 0
noresult = 0
nopublishTime = 0

for dic in data:
	if(dic.__contains__('visitTimes') == False):
		novisitTimes += 1
	if(dic.__contains__('result') == False):
		noresult += 1
	if(dic.__contains__('publishTime') == False):
		nopublishTime += 1
	

print('{} data has no visitTimes'.format(novisitTimes))			##1条数据没有visitTimes
print('{} data has no result'.format(noresult))					##334条数据没有result
print('{} data has no publishTime'.format(nopublishTime))		##23条数据没有publishTime

##5保存data

savefile = "datap/alldata.json"
with open(savefile,'w') as fp:
	for x in data:
		dicc = json.dumps(x,ensure_ascii=False)
		fp.write(dicc)
		fp.write('\n')

