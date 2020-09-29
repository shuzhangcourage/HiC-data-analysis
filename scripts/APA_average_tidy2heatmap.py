#!/bin/bash
import sys

APA=open(sys.argv[1])
output=open(sys.argv[2],"w")
maxi=sys.argv[3]
def tidy():
	list_APA=[]
	w=(maxi+'\t')+("NA"+"\t")*15+maxi+"\n"
	output.write(w)
	w=(maxi+'\t')+("NA"+"\t")*15+maxi+"\n"
	output.write(w)
	for eachline in APA:
		line=eachline.strip().split("\t")
		w=("NA"+"\t")*2
		for i in line:
			w=w+i+"\t"
		w=w+"NA"+"\t"+"NA"+"\n"
		output.write(w)
	w=(maxi+'\t')+("NA"+"\t")*15+maxi+"\n"
	output.write(w)
	w=(maxi+'\t')+("NA"+"\t")*15+maxi+"\n"
	output.write(w)
	return 

tidy()
		
		
