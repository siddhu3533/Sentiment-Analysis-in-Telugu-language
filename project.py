import subprocess
p = subprocess.Popen('exec '+'make tag',cwd='/home/siddhu/telugu-part-of-speech-tagger/',shell =True,)
p.wait()
file2 = open('/home/siddhu/Documents/Positive3.py','w')
set1 = set(line.strip() for line in open('/home/siddhu/Documents/Telugu_SentiWordNet/TE_POS.txt'))
set2 = set()
# for i in set1:
#  	j = i.split('	')
#  	set2.add(j[1])
file1 = open('/home/siddhu/telugu-part-of-speech-tagger/telugu.output.txt','r')
list1 = file1.readlines()
for i in list1:
	j = i.split('	')
	if(len(j)>2):
		set2.add(j[1])
for i in set2:
	file2.write('"'+i+'"'',')
print 'end'
