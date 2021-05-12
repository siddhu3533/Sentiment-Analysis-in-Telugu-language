#!/usr/bin/python
#!/usr/bin/env python
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import codecs
import subprocess
from Tkinter import *

def executeProjectCode():
	e2.delete(0,END)
	input1 = codecs.open('/home/siddhu/Documents/Input.txt','w',encoding = 'utf-8')
	input1.write(e1.get())
	input1.close()
	p = subprocess.Popen('exec '+'python projectCode1.py',cwd='/home/siddhu/Documents/',shell =True,)
	p.wait()
	e1.delete(0,END)
	Output = open('/home/siddhu/Documents/Output.txt','r')
	s = Output.read()
	if s =='yes':
		e2.insert(10,'Positive')
	elif s == 'no':
		e2.insert(10,'Negative')
	else:
		e2.insert(10,'Neutral')



master = Tk()
Label(master, text="Input Text").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)
Button(master, text='Find Sentiment', command=executeProjectCode).grid(row=1, column=1, sticky=W, pady=4)

Label(master, text="Output").grid(row=2)

e2 = Entry(master)
e2.grid(row=2, column=1)
mainloop( )
