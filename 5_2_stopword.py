filename = "datap/stopword.txt" 
savefile = "datap/stop_word.txt"
result = list() 
with open(filename,'r',encoding = 'utf-8') as f: 
	for line in f.readlines(): 
		line = line.strip() 
		if not len(line): 
			continue 
		result.append(line) 

with open(savefile,"w",encoding='utf-8') as fw: 
	for sentence in result: 
		sentence.encode('utf-8') 
		data=sentence.strip() 
		if len(data)!=0: 
			fw.write(data) 
			fw.write("\n") 
print ("end")
