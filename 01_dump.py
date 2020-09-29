#!/bin/python

import sys
import os

## Utilize Dump from https://github.com/aidenlab/juicer/wiki/Data-Extraction

juicertools="java -Djava.awt.headless=true -Xmx32000m -jar juicer_tools_1.13.02.jar dump"
scriptpath="./scripts/addChr2dump.py"
method=sys.argv[1]## <observed/oe> <norm/expected> <loops/domains>
normalization=sys.argv[2]## <NONE/VC/VC_SQRT/KR>
hicfile=sys.argv[3]##hic file
delimited=sys.argv[4]##<BP/FRAG>
binsize=sys.argv[5]#<2500000, 1000000, 500000, 250000, 100000, 50000, 25000, 10000, 5000>
output=sys.argv[6]#output
name=sys.argv[7]#name of sample
command="mkdir -p dump"
os.system(command)

output="dump/"+output+"/"

##normal setting
## <observed/oe> <NONE/VC/VC_SQRT/KR> <hicFile(s)> <chr1>[:x1:x2] <chr2>[:y1:y2] <BP/FRAG> <binsize> [outfile]
## <norm/expected> <NONE/VC/VC_SQRT/KR> <hicFile(s)> <chr> <BP/FRAG> <binsize> [outfile]

def dump():
	command="mkdir -p " + output
	os.system(command)
	for i in range(1,24):
		if i==23:
			i="X"
			filename=output + name+"_chr"+str(i)+"_"+binsize+".xls"
			command=" ".join([juicertools,method,normalization,hicfile,i,i,delimited,binsize,filename])
			print(command)
			os.system(command)
			Chr="chr"+str(i) 
			addout=output + name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
			command=" ".join(["python",scriptpath,Chr,filename,addout])
			print(command)
			os.system(command)
		else:
			filename=output + name+"_chr"+str(i)+"_"+binsize+".xls"
			command=" ".join([juicertools,method,normalization,hicfile,str(i),str(i),delimited,binsize,filename]) 
			os.system(command)
			Chr="chr"+str(i)
			addout=output + name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
			command=" ".join(["python",scriptpath,Chr,filename,addout])
			os.system(command)

	command = "cat " + output + name+"_chr*_"+binsize+".addChr.xls" + " > "+ output + "all_"+name+"_"+binsize+".addChr.xls" 
	os.system(command)

	return

dump()
