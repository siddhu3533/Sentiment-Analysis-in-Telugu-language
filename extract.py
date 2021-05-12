file2 = open('/home/siddhu/telugu-part-of-speech-tagger/telugu.input.txt','w')
set1 = list(line.split(' ') for line in open('/home/siddhu/Downloads/telugu_words'))
for i in set1:
	for j in i:
		file2.write(j+'\n')
