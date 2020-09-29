import sys
from sys import argv

'''
usage python 03_reordered_oe_value.py  sort_position.txt dumpoe reordered_oe_file
'''

inputpos=open(sys.argv[1],'r')
inputoe=open(sys.argv[2],'r')
output=open(sys.argv[3],'w')

dict_pos={}

for eachline in inputpos:
	line=eachline.strip().split()
	binnu=line[-1]
	key=line[0]+'_'+line[1]
	dict_pos[key]=binnu
	
for eachline in inputoe:
	line=eachline.strip().split()
	key1=line[0]+'_'+line[1]
	key2=line[0]+'_'+line[2]
	if key1 in dict_pos and key2 in dict_pos:
		start=int(dict_pos[key1])
		end=int(dict_pos[key2])
		value=line[-1]
		w=str(start)+'\t'+str(end)+'\t'+value+"\n"
		output.write(w)

inputpos.close()
inputoe.close()
output.close()
	
