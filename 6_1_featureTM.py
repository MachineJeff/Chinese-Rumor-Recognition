import numpy as np
import json

file = "datap/data_1.json" 
data = []
with open(file,"r") as fp:
	for line in fp.readlines():
		data.append(json.loads(line))


features = set()

for x in data:
	del x['text']
	for key in x.keys():
		features.add(key)

print(features)

for x in 
