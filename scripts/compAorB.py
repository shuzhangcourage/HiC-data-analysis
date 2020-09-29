#!/usr/bin/python

import sys
from sys import argv

'''
Usage
python AorB.py BED_signal eigenvector Outfile 
'''

ChIPfile=open(sys.argv[1],'r')
Compartmentfile=open(sys.argv[2],'r')
outfile=open(sys.argv[3],'w')

dict_ChIPfile={}
index_ChIPfile=0
index_Compartmentfile=0
Compartmentfile_above=0
Compartmentfile_below=0

for eachline in ChIPfile:
	line=eachline.strip('\n').split('\t')
	if line[0]=='Chr':
		w=eachline.strip('\n')+'\t'+"eigenvector"+'\t'+"Compartment"+'\n'
		outfile.write(w)
	else:
		index_ChIPfile+=1
		dict_ChIPfile[index_ChIPfile]=[0,0]
		dict_ChIPfile[index_ChIPfile][0]=float(line[-1])	
		dict_ChIPfile[index_ChIPfile][1]=eachline.strip('\n')

for eachline in Compartmentfile:
	line=eachline.strip('\n')
	index_Compartmentfile+=1
	if line != "NaN":
		if float(line) > 0:
			Compartmentfile_above+=dict_ChIPfile[index_Compartmentfile][0]
		if float(line) < 0:
			Compartmentfile_below+=dict_ChIPfile[index_Compartmentfile][0]

Compartmentfile.seek(0)
index_Compartmentfile=0
print (Compartmentfile_above,Compartmentfile_below)
if Compartmentfile_above > Compartmentfile_below:
	for eachline in Compartmentfile:
		line=eachline.strip('\n')
		index_Compartmentfile+=1		
		if line != "NaN":
			if float(line) > 0:
				w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"A"+'\n'
				outfile.write(w)
			if float(line) < 0:
				w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"B"+'\n'
				outfile.write(w)
		else:
			w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"unknow"+'\n'
			outfile.write(w)

if Compartmentfile_above < Compartmentfile_below:
	for eachline in Compartmentfile:
		line=eachline.strip('\n')
		index_Compartmentfile+=1
		if line!="NaN":
			if float(line) > 0:
				w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"B"+'\n'
				outfile.write(w)
			if float(line) < 0:
				w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"A"+'\n'
				outfile.write(w)
		else:
			w=dict_ChIPfile[index_Compartmentfile][1]+'\t'+line+'\t'+"unknow"+'\n'
			outfile.write(w)

Compartmentfile.close()
ChIPfile.close()
