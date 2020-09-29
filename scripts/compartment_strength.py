import sys
import numpy
from sys import argv
from numpy import median

'''
usage 
python medium.py modify_dump ev1_top20_pos 
'''

inputoe=open(sys.argv[1],'r')
inputev1pos=open(sys.argv[2],'r')

EVa=[]
EVb=[]

chro={}
for eachline in inputev1pos:
	line=eachline.strip().split('_')		
	if line[-1]=="A":
		EVa.append(line[0]+'_'+line[1])
	if line[-1]=="B":
		EVb.append(line[0]+'_'+line[1])

#print (EVa)

for eachline in inputoe:
	line=eachline.strip().split()
	bin1=line[0]+'_'+line[1]
	bin2=line[0]+'_'+line[2]
	if line[0] in chro:
		if bin1 in EVa and bin2 in EVa and line[-1]!='NaN':
			chro[line[0]][0].append(float(line[-1]))
		if bin1 in EVb and bin2 in EVb and line[-1]!='NaN':
			chro[line[0]][1].append(float(line[-1]))
		if bin1 in EVa and bin2 in EVb and line[-1]!='NaN':
			chro[line[0]][2].append(float(line[-1]))
		if bin1 in EVb and bin2 in EVa and line[-1]!='NaN':
			chro[line[0]][3].append(float(line[-1]))
	if line[0] not in chro:
		chro[line[0]]=[[],[],[],[]]
		if bin1 in EVa and bin2 in EVa and line[-1]!='NaN':
			chro[line[0]][0].append(float(line[-1]))
		if bin1 in EVb and bin2 in EVb and line[-1]!='NaN':
			chro[line[0]][1].append(float(line[-1]))
		if bin1 in EVa and bin2 in EVb and line[-1]!='NaN':
			chro[line[0]][2].append(float(line[-1]))
		if bin1 in EVb and bin2 in EVa and line[-1]!='NaN':
			chro[line[0]][3].append(float(line[-1]))
	
for i in chro:
	s1=median(chro[i][0])+median(chro[i][1])
	if chro[i][2]!=[] and chro[i][3]!=[]:
		s2=median(chro[i][2])+median(chro[i][3])
		print(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2))
	elif chro[i][2]!=[] and chro[i][3]==[]:
		s2=2*median(chro[i][2])
		print(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2))
	elif chro[i][2]==[] and chro[i][3]!=[]:
		s2=2*median(chro[i][3])
		print(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2))


inputoe.close()
inputev1pos.close()
