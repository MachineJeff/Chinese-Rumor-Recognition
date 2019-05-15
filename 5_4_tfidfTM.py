from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

file = "datap/jieba.txt"
corpus = []

with open(file,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		corpus.append(line)

print(len(corpus))


vectorizer=CountVectorizer()

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  

tag = []
tagfile = "datap/tagList.txt"
with open (tagfile,"r") as fp:
	for line in fp.readlines():
		line = line.strip('\n')
		if(line == "False"):
			tag.append(0)
		else:
			tag.append(1)

print(tag[:2])


volume = (len(corpus)//3) *2
print(volume)

x_train = tfidf[:volume,]
y_train = tag[:volume]

x_test = tfidf[volume:,]
y_test = tag[volume:]


clf = MultinomialNB(alpha = 0.01)
clf.fit(x_train,y_train)
score = clf.score(x_train,y_train)
print(score)

pre = clf.predict(x_test)

print(clf)
print(classification_report(y_test,pre))

cm = confusion_matrix(y_test,pre)
print(cm)


poo = clf.predict_proba(x_train)

print(poo)

ok = "datap/tfidfPro.txt"
with open(ok,"w") as fp:
	for x in poo:
		fp.write(str(x[0]))
		fp.write("\n")
