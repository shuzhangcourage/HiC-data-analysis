#!/bin/python

import sys
from sys import argv

input=open(sys.argv[1])
output=open(sys.argv[2],"w")
def heatmapmatrix(input,output):
	dictvalue={}
	listnumber=[]
	for eachline in input:
		line=eachline.strip().split()
		if line[2]!="NaN":
			if int(line[0]) not in listnumber:
				listnumber.append(int(line[0]))
			if int(line[1]) not in listnumber:
				listnumber.append(int(line[1]))
			key1=line[0]+":"+line[1]
			key2=line[1]+":"+line[0]
			dictvalue[key1]=line[2]
			dictvalue[key2]=line[2]

	listnumber.sort()
	length=len(listnumber)
	sections=length//49
	number = length/sections
	dict_sections={}

	for i in range(0,50):
		for j in range(0,50):
			dict_sections[str(i)+":"+str(j)]=[0,0]
	
	for i in range(0,length):
		row=i//sections
		for j in range(0,length):
			col=j//sections
			key=str(listnumber[i])+":"+str(listnumber[j])
			if row > 49:
				row=49
			if col > 49:
				col=49
			new_key=str(row)+":"+str(col)
			if key in dictvalue:
				if new_key in dict_sections:
					dict_sections[new_key][0]+=float(dictvalue[key])
					dict_sections[new_key][1]+=1

#	for i in range(0,50):
#		w=''
#		for j in range(0,50):
#			if dict_sections[str(i)+":"+str(j)][0]!=0:
#				w+=str(dict_sections[str(i)+":"+str(j)][0]/dict_sections[str(i)+":"+str(j)][1])+"\t"
#			if dict_sections[str(i)+":"+str(j)][0]==0:
#				w+="NA"+"\t"
#		w=w.strip("\t")+"\n"
#		output.write(w)
	for i in dict_sections:
		if dict_sections[i][1] != 0:
			w=i+"\t"+str(dict_sections[i][0]/dict_sections[i][1])+"\n"
			output.write(w)
		if dict_sections[i][1] == 0:
			w=w=i+"\t"+"NA"+"\n"  			
			output.write(w)
					
	return

heatmapmatrix(input,output)
