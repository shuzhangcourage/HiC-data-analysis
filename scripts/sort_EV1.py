import sys
from sys import argv 

'''
Usage python 01_reorder_EV1.py EV1 reorder_EV1
'''

input=open(sys.argv[1],'r')
output=open(sys.argv[2],'w')

list_EV_A=[]
list_EV_B=[]
dict_all_pos={}
for eachline in input:
	line=eachline.strip().split()
	if line[0]!='Chr':
		if abs(float(line[-2])) in dict_all_pos:
			print('same EV1') #all values are them unique
		if line[-1]=='A':
			list_EV_A.append(abs(float(line[-2])))
			dict_all_pos[abs(float(line[-2]))]=line[0]+'\t'+line[1]+'\t'+str(abs(float(line[-2])))
		if line[-1]=='B':
			list_EV_B.append(-1*(abs(float(line[-2]))))
			dict_all_pos[-1*(abs(float(line[-2])))]=line[0]+'\t'+line[1]+'\t'+str(-1*abs(float(line[-2])))

list_EV_A.sort()
list_EV_B.sort()
count=0
for i in list_EV_B:
	count+=1
	w=dict_all_pos[i]+'\t'+str(count)+"\n"
	output.write(w)
for i in list_EV_A:
	count+=1
	w=dict_all_pos[i]+'\t'+str(count)+"\n"
	output.write(w)
del list_EV_A
del list_EV_B
del dict_all_pos

input.close()
output.close()
