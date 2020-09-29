#!/bin/python

import sys
import os

#juicer_tools eigenvector -p <NONE/VC/VC_SQRT/KR> <hicFile(s)> <chr> <BP/FRAG> <binsize> [outfile]

juicertools="java -Djava.awt.headless=true -Xmx32000m -jar juicer_tools_1.13.02.jar eigenvector -p"
scriptpath="./scripts/compAorB.py"
genedensity="compartment_genedensity_250K/"
normalization=sys.argv[1]## <NONE/VC/VC_SQRT/KR>
hicfile=sys.argv[2]##hic file
delimited=sys.argv[3]##<BP/FRAG>
binsize=sys.argv[4]#<In general is 250000>
output=sys.argv[5]#output
name=sys.argv[6]#name of sample
command="mkdir -p EV1"
os.system(command)

output="EV1/"+output+"/"

def EV1():
	command="mkdir -p " + output
	os.system(command)
	for i in range(1,24):
		if i==23:
			i="X"
			filename=output + name+"_chr"+str(i)+"_"+binsize+".xls"
			command=" ".join([juicertools,normalization,hicfile,i,delimited,binsize,filename])
			print(command)
			os.system(command)
			densityfile=genedensity+"chr"+str(i)+"_"+binsize+"_genedensity.xls"
			addout=output + name+"_chr"+str(i)+"_"+binsize+".AorB.xls"
			command=" ".join(["python",scriptpath,densityfile,filename,addout])
			print(command)
			os.system(command)
		else:
			filename=output + name+"_chr"+str(i)+"_"+binsize+".xls"
			command=" ".join([juicertools,normalization,hicfile,str(i),delimited,binsize,filename]) 
			print(command)
			os.system(command)
			densityfile=genedensity+"chr"+str(i)+"_"+binsize+"_genedensity.xls"
			addout=output + name+"_chr"+str(i)+"_"+binsize+".AorB.xls"
			command=" ".join(["python",scriptpath,densityfile,filename,addout])
			print(command)
			os.system(command)
	
	command = "cat "+ output + name+"_chr*_"+binsize+".AorB.xls > " +  output+"all_"+name+"_"+binsize+".AorB.xls"
	os.system(command)
	return

EV1()
