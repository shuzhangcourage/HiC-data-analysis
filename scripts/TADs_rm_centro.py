#!/bin/bash
import sys

infile=open(sys.argv[1])
centromere=open(sys.argv[2])
output=open(sys.argv[3],'w')
def rmCentromere():
	dict_centromere={}
	for eachline in centromere:
		line=eachline.strip().split()
		key=line[0]
		dict_centromere[key]=[int(line[1]),int(line[2])]
#	print(dict_centromere)
	for eachline in infile:
		line=eachline.strip().split()
		key="chr"+line[0]	
		#pos=(int(line[1])+int(line[2]))/2
		if int(line[1]) >=dict_centromere[key][1] or int(line[2]) <= dict_centromere[key][0]:
			output.write(eachline)
	return

rmCentromere()
		
