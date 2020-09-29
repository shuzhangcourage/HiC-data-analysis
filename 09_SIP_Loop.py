#!/bin/python

import sys
import os

SIP="SIP_HiC.jar "
genome="chrom.sizes.hg38.filter "
juicertools="juicer_tools_1.13.02.jar "

hicfile=sys.argv[1] ##hic file
output=sys.argv[2] #name of output
resolution=sys.argv[3]
matrix=sys.argv[4]
guss=sys.argv[5]
fdr=sys.argv[6]
distance=sys.argv[7]
nbzero=sys.argv[8]

#normal setting
#25K: -res 25000 -mat 800 -g 2 -fdr 0.01/0.05 -d 3 -nbZero 3 
#10K: -res 10000  -mat 2000 -g 2 -fdr 0.01/0.05 -d 3 -nbZero 4
#5K: -res 5000 -mat 4000 -g 2 -fdr 0.01/0.05 -d 6 -nbZero 6
def SIP():	
	command="mkdir -p SIP_Loop"
	os.system(command)
	output="SIP_Loop/"+output
	command = " java -jar " + SIP + " hic " + hicfile + genome + output + juicertools + " -res " + resolution + " -mat " + matrix + " -g " + guss + " -fdr " + fdr + " -d " + distance + " -nbZero " + nbzero
	os.system(command)
	return
SIP()
