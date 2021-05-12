 # -*- coding: utf-8 -*-
import subprocess
import common
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
	if i in open('StopWords1.py').read():
		list3.remove(i)
 	elif i in common.neutral:
	 	print 'neu'
	 	print i
		count+=0
	elif i in common.negative:
		print 'neg'
		print i
		count-=1
	elif i in common.positive:
		print 'posi'
		print i
		count+=1
	else:
		count+=0
Output = open('/home/siddhu/Documents/Output.txt','w')
if count>0:
	Output.write('yes')
elif count<0:
	Output.write('no')
else:
	Output.write('neutral')
print 'end'
