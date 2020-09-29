#!/bin/python

import sys
from sys import argv

"""
usage python DI.py chromsize observed.tidyall output
"""
chromsize = sys.argv[1]
observed = sys.argv[2]
DI_output = sys.argv[3]
def DI(chromsize,observed,DI_output):

#	binsize=40000
	binsize=int(sys.argv[4])
#	upstream=2000000
#	downstream=2000000
	upstream=int(sys.argv[5])
	downstream=int(sys.argv[5])
	dict_DI={}
	list_DI=[]
	with open(chromsize) as chromsize, open(observed) as observed, open(DI_output,'w') as DI_output:
		for eachline in chromsize:
			line=eachline.strip().split()
			for i in range(0,int(line[1]),binsize):
				if i - upstream >0 and i+downstream < int(line[1]):
					key = line[0]+":"+str(i)
					dict_DI[key]=[0,0]
					list_DI.append(key)
		for eachline in observed:
			line=eachline.strip().split()
			firstbin = int(line[1])
			secondbin = int(line[2])
			key1=line[0]+":"+str((firstbin//binsize)*binsize)
			key2=line[0]+":"+str((secondbin//binsize)*binsize)
			if firstbin != secondbin and binsize < secondbin - firstbin <upstream and line[3] != "NaN":
				if key1 in dict_DI:
					dict_DI[key1][1]+=float(line[3])
				if key2 in dict_DI:
					dict_DI[key2][0]+=float(line[3])	
		for i in list_DI:
			A=dict_DI[i][0]
			B=dict_DI[i][1]
			E=float((A+B)/2)
			if E!=0 and abs(B-A)!=0:
				a=(A-E)*(A-E)
				b=(B-E)*(B-E)
				DI=((B-A)/abs(B-A))*((a/E)+(b/E))
				#w=i.split(":")[0][3:]+"\t"+i.split(":")[1]+"\t"+str(int(i.split(":")[1])+binsize)+"\t"+str(A)+"\t"+str(B)+"\t"+str(DI)+"\n"
				w=i.split(":")[0][3:]+"\t"+i.split(":")[1]+"\t"+str(int(i.split(":")[1])+binsize)+"\t"+str(DI)+"\n"
				DI_output.write(w)
	return

DI(chromsize,observed,DI_output)
