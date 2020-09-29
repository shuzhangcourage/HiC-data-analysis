#!/bin/python 

import sys
from sys import argv

input=open(sys.argv[1],'r')
output=open(sys.argv[2],'w')
binsize=sys.argv[3]

dict={}
list=[]
for eachline in input:
	line=eachline.strip().split()
	if line[3]!='NaN':
		disbin=abs((int(line[2])-int(line[1]))/10000)
		if disbin in dict:
			dict[disbin][0]+=float(line[3])
		if disbin not in dict:
			list.append(disbin)
			dict[disbin]=[0]
			dict[disbin][0]+=float(line[3])
list.sort()

for i in list:	
	w= str(i) + '\t' + str(float(dict[i][0]))+ '\n'
	output.write(w)

input.close()
output.close()
