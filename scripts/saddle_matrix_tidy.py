#!/bin/python
import sys
from sys import argv

input=open(sys.argv[1])
output=open(sys.argv[2],"w")

def merge2heatmap(input, output):
	dictmerge={}
	for eachline in input:
		line=eachline.strip().split()
		if line[1]!="NA":
			key=line[0]
			if key in dictmerge:
				dictmerge[key][0]+=float(line[1])
				dictmerge[key][1]+=1
			if key not in dictmerge:
				dictmerge[key]=[float(line[1]),1]
	for i in range(0,50):
		w=''
		for j in range(0,50):
			if str(i)+":"+str(j) not in dictmerge or dictmerge[str(i)+":"+str(j)][1] < 5 :
				w=w+"NA"+"\t"
			else: #dictmerge[str(i)+":"+str(j)][1] !=0 :
				w=w+str(dictmerge[str(i)+":"+str(j)][0]/dictmerge[str(i)+":"+str(j)][1])+"\t"
		w=w.strip("\t")+"\n"
		output.write(w)
	return

merge2heatmap(input, output)
