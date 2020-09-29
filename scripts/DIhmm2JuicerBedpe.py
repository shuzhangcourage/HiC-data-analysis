#!/usr/bin/python

import sys
from sys import argv

'''
Usage
python DI2Juicer.py DI.out juicer.bed
'''

infile=open(sys.argv[1],'r')
outfile=open(sys.argv[2],'w')

w='#chr1'+'\t'+'x1'+'\t'+'x2'+'\t'+'chr2'+'\t'+'y1'+'\t'+'y2'+'\t'+'name'+'\t'+'score'+'\t'+'strand1'+'\t'+'strand2'+'\t'+\
            'color'+'\t'+'score'+'\t'+'uVarScore'+'\t'+'lVarScore'+'\t'+'upSign'+'\t'+'loSign'+'\n'
outfile.write(w)
w='#juicer_tools version 1.11.09'+'\n'
outfile.write(w)

for eachline in infile:
	line=eachline.strip('\n').split('\t')
	if line[2]!="" and line[0][3:]!="23":
		w=line[0][3:]+'\t'+line[1]+'\t'+line[2]+'\t'+line[0][3:]+'\t'+line[1]+'\t'+line[2]+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'255,255,0'+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'\n'
		outfile.write(w)
	if line[2]!="" and line[0][3:]=="23":
		w="X"+'\t'+line[1]+'\t'+line[2]+'\t'+"X"+'\t'+line[1]+'\t'+line[2]+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'255,255,0'+'\t'+'.'+'\t'+'.'+'\t'+'.'+'\t'+'\n'
		outfile.write(w)

infile.close()
outfile.close()


