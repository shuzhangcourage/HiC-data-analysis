import sys
from sys import argv 

'''
Usage python count_20percent_EV1.py ./EV1/file top20%percentEV1
'''

input=open(sys.argv[1],'r')
output=open(sys.argv[2],'w')

dict_EV_A={}
dict_EV_B={}
dict_all_pos={}
for eachline in input:
	line=eachline.strip().split()
	if line[0]!='Chr':
		if line[0] in dict_EV_A:
			if abs(float(line[-2])) in dict_all_pos:
				print('same EV1') #all values are them unique
			if line[-1]=='A':
				dict_EV_A[line[0]].append(abs(float(line[-2])))
				dict_all_pos[abs(float(line[-2]))]=line[0]+'_'+line[1]
			if line[-1]=='B':
				dict_EV_B[line[0]].append(abs(float(line[-2])))
				dict_all_pos[abs(float(line[-2]))]=line[0]+'_'+line[1]
		if line[0] not in dict_EV_A:
			dict_EV_A[line[0]]=[]
			dict_EV_B[line[0]]=[]
			if line[-1]=='A':
				dict_EV_A[line[0]].append(abs(float(line[-2])))
				dict_all_pos[abs(float(line[-2]))]=line[0]+'_'+line[1]
			if line[-1]=='B':
				dict_EV_B[line[0]].append(abs(float(line[-2])))
				dict_all_pos[abs(float(line[-2]))]=line[0]+'_'+line[1]

for i in dict_EV_A:
	dict_EV_A[i].sort()
	dict_EV_B[i].sort()
for i in dict_EV_A:
	for n in range(len(dict_EV_A[i])-int(len(dict_EV_A[i])*0.2),len(dict_EV_A[i]),1):
		key=dict_EV_A[i][n]
		w=dict_all_pos[key]+'_'+'A'+'\n'
		output.write(w)

for i in dict_EV_B:
	for n in range(len(dict_EV_B[i])-int(len(dict_EV_B[i])*0.2),len(dict_EV_B[i]),1):
		key=dict_EV_B[i][n]
		w=dict_all_pos[key]+'_'+'B'+'\n'
		output.write(w)

input.close()
output.close()
