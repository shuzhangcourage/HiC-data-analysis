import sys
from sys import argv

'''
usage python chrnumber dump out
'''

input1=sys.argv[1]
input2=open(sys.argv[2],'r')
out=open(sys.argv[3],'w')

chr=input1
for eachline in input2:
	w=chr+'\t'+eachline.strip()+'\n'
	out.write(w)

input2.close()
out.close()


