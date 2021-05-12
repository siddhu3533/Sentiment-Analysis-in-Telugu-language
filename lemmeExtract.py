file2 = open('/home/siddhu/Documents/positive.py','w')
set1 = list(line.split(' ') for line in open('/home/siddhu/Documents/Telugu_SentiWordNet/TE_POS.txt'))
for i in set1:
	if len(i) > 1:
		file2.write(i[1])
