#!/bin/bash
import sys

APA=open(sys.argv[1])
output=open(sys.argv[2],"w")
number=int(sys.argv[3])

def tidy():
	list_APA=[]
		
	for eachline in APA:
		line=eachline.strip()[1:-1]
		line=line.split(", ")
		w=''
		for i in line:
			list_APA.append(float(i)/number)
			w=w+str(float(i)/number)+"\t"
		w=w.strip("\t")+"\n"
		output.write(w)
	Max=max(list_APA)
	print(Max)
	return 

tidy()
		
		
