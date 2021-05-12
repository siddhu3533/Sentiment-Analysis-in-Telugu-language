from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import subprocess
file1 = open('/home/siddhu/telugu-part-of-speech-tagger/telugu.input.txt','w')
input1 = open('/home/siddhu/Documents/Input.txt','r')
list1 = input1.readlines()
for i in list1:
	j = i.split(' ')
	for k in j:
		file1.write(k+'\n')
file1.close()		
p = subprocess.Popen('exec '+'make tag',cwd='/home/siddhu/telugu-part-of-speech-tagger/',shell =True,)
p.wait()
file2 = open('/home/siddhu/telugu-part-of-speech-tagger/telugu.output.txt','r')		
list2 = file2.readlines()
list3 = []
for i in list2:
	j = i.split('	')
	if len(j)>2:
		list3.append(j[1])
count = 0	
for i in list3:
	if i in open('StopWords.py').read():
		list3.remove(i)
list4=[]
for i in open('Positive.py').readlines():
	list4.append([i[0:-1],'1'])
list5=[]
for i in open('Negative.py').readlines():
	list5.append([i[0:-1],'-1'])
list6=[]
for i in open('Neutral.py').readlines():
	list6.append([i[0:-1],'0'])		
final_list = list4 + list5 + list6
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform([r[0] for r in final_list])
test_features = vectorizer.transform([r[0] for r in list3])
nb = MultinomialNB()
nb.fit(train_features, [int(r[1]) for r in reviews])
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))