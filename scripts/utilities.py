#!/home/uni08/szhang3/Software/Python-3.8.0/bin/python3.8

import sys,os
import numpy
from numpy import median

def addChromosome(Chr,DumpOutFile,addchrout):
	with open(DumpOutFile) as dumpoutfile, open(addchrout,'w') as addchrout:
		for eachline in dumpoutfile:
			addchrout.write(Chr+'\t'+eachline.strip()+'\n')
	dumpoutfile.close()
	addchrout.close()
	return
			
def dump(juicertools,method,normalization,hicfile,delimited,binsize,samplename,outdir):
	command="mkdir -p " + outdir
	os.system(command)
	for i in range(1,24):
		if i==23:
			i="X"
			outname=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".xls"
			command=" ".join([juicertools,method,normalization,hicfile,i,i,delimited,binsize,outname])
			os.system(command)
			Chr="chr"+str(i) 
			addchrout=outdir + samplename+"_chr" + str(i) + "_" + binsize + ".addChr.xls"
			DumpOutFile=outname
			addChromosome(Chr,DumpOutFile,addchrout)
		else:
			outname=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".xls"
			command=" ".join([juicertools,method,normalization,hicfile,str(i),str(i),delimited,binsize,outname]) 
			os.system(command)
			Chr="chr"+str(i)
			addchrout=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".addChr.xls"
			DumpOutFile=outname
			addChromosome(Chr,DumpOutFile,addchrout)
	return


def mergeAllDump(outdir,samplename,binsize):
	command=" ".join(["cat",outdir+samplename+"*"+binsize+".addChr.xls",">",outdir+"all_"+samplename+"_"+binsize+".addChr.xls"])
	os.system(command)

def calEV1(juicertools,normalization,hicfile,delimited,binsize,samplename,outdir,geneDensityFolder):
	command="mkdir -p " + outdir
	os.system(command)
	for i in range(1,24):
		if i==23:
			i="X"
			outname=outdir + samplename + "_chr" + str(i) +"_" + binsize + ".xls"
			command=" ".join([juicertools,normalization,hicfile,i,delimited,binsize,outname])
			os.system(command)
			densityfile=geneDensityFolder + "chr" + str(i) + "_" + binsize + "_genedensity.xls"
			EV1outname=outname
			AorB(densityfile,EV1outname,outdir,samplename,i,binsize)
		else:
			outname=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".xls"
			command=" ".join([juicertools,normalization,hicfile,str(i),delimited,binsize,outname]) 
			os.system(command)
			densityfile=geneDensityFolder + "chr" + str(i) + "_" + binsize + "_genedensity.xls"
			EV1outname=outname
			AorB(densityfile,EV1outname,outdir,samplename,i,binsize)
	return

def AorB(densityfile,EV1outname,outdir,samplename,i,binsize):
	addAorB=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.xls"
	with open(densityfile) as densityfile, open(EV1outname) as EV1outname, open(addAorB,'w') as addAorB: 	
		dict_densityfile={}
		index_densityfile=0
		index_EV1outname=0
		EV1outname_above=0
		EV1outname_below=0
		for eachline in densityfile:
			line=eachline.strip('\n').split('\t')
			if line[0]=='Chr':
				addAorB.write(eachline.strip('\n')+'\t'+"eigenvector"+'\t'+"Compartment"+'\n')
			else:
				index_densityfile+=1
				dict_densityfile[index_densityfile]=[0,0]
				dict_densityfile[index_densityfile][0]=float(line[3])	
				dict_densityfile[index_densityfile][1]=eachline.strip('\n')

		for eachline in EV1outname:
			line=eachline.strip('\n')
			index_EV1outname+=1
			if line != "NaN":
				if float(line) > 0:
					EV1outname_above+=dict_densityfile[index_EV1outname][0]
				if float(line) < 0:
					EV1outname_below+=dict_densityfile[index_EV1outname][0]
	
		EV1outname.seek(0)
		index_EV1outname=0
		if EV1outname_above > EV1outname_below:
			for eachline in EV1outname:
				line=eachline.strip('\n')
				index_EV1outname+=1		
				if line != "NaN":
					if float(line) > 0:
						addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"A"+'\n')
					if float(line) < 0:
						addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"B"+'\n')
				else:
					addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"unknow"+'\n')
		if EV1outname_above < EV1outname_below:
			for eachline in EV1outname:
				line=eachline.strip('\n')
				index_EV1outname+=1
				if line!="NaN":
					if float(line) > 0:
						addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"B"+'\n')
					if float(line) < 0:
						addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"A"+'\n')
				else:
					addAorB.write(dict_densityfile[index_EV1outname][1]+'\t'+line+'\t'+"unknow"+'\n')
		
		EV1outname.close()
		densityfile.close()
		del dict_densityfile
	return

def sort_EV1(outdir,samplename,binsize,i):
	list_EV_A=[]
	list_EV_B=[]
	dict_all_pos={}
	addAorB=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.xls"
	addAorBsort=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.xls"
	with open(addAorB) as addAorB, open(addAorBsort,'w') as addAorBsort:
		for eachline in addAorB:
			line=eachline.strip().split()
			if line[0]!='Chr' and abs(float(line[-2])) in dict_all_pos:
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
			addAorBsort.write(dict_all_pos[i]+'\t'+str(count)+"\n")
		for i in list_EV_A:
			count+=1
			addAorBsort.write(dict_all_pos[i]+'\t'+str(count)+"\n")
	addAorB.close()
	addAorBsort.close()
	del list_EV_A;list_EV_B;dict_all_pos

def dumpOEmatchEV1sortref(outdir,samplename,binsize,i):
	dumpOE="dump/OE_250K/" + samplename + "_chr" + str(i) + "_" + binsize + ".addChr.xls"
	addAorBsort=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.xls"
	addAorBsortmatchDumpOE=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.addOE.xls"
	dict_pos={}
	with open(dumpOE) as dumpOE, open(addAorBsort) as addAorBsort, open(addAorBsortmatchDumpOE,'w') as addAorBsortmatchDumpOE:
		for eachline in addAorBsort:
			line=eachline.strip().split()
			binnu=line[-1]
			key=line[0]+'_'+line[1]
			dict_pos[key]=binnu
		for eachline in dumpOE:
			line=eachline.strip().split()
			key1=line[0]+'_'+line[1]
			key2=line[0]+'_'+line[2]
			if key1 in dict_pos and key2 in dict_pos:
				start=int(dict_pos[key1])
				end=int(dict_pos[key2])
				value=line[-1]
				addAorBsortmatchDumpOE.write(str(start)+'\t'+str(end)+'\t'+value+"\n")
	addAorBsort.close()
	addAorBsortmatchDumpOE.close()
	del dict_pos
def dumpOEmatchEV1sort(outdir,samplename,binsize,i,sampleref):
	dumpOE="dump/OE_250K/" + samplename + "_chr" + str(i) + "_" + binsize + ".addChr.xls"
	addAorBsort=outdir + sampleref + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.xls"
	addAorBsortmatchDumpOE=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.addOE.xls"
	dict_pos={}
	with open(dumpOE) as dumpOE, open(addAorBsort) as addAorBsort, open(addAorBsortmatchDumpOE,'w') as addAorBsortmatchDumpOE:	
		for eachline in addAorBsort:
			line=eachline.strip().split()
			binnu=line[-1]
			key=line[0]+'_'+line[1]
			dict_pos[key]=binnu
		for eachline in dumpOE:
			line=eachline.strip().split()
			key1=line[0]+'_'+line[1]
			key2=line[0]+'_'+line[2]
			if key1 in dict_pos and key2 in dict_pos:
				start=int(dict_pos[key1])
				end=int(dict_pos[key2])
				value=line[-1]
				addAorBsortmatchDumpOE.write(str(start)+'\t'+str(end)+'\t'+value+"\n")
	addAorBsort.close()
	addAorBsortmatchDumpOE.close()
	del dict_pos
def saddleMatrix(outdir,samplename,binsize,i):
	addAorBsortmatchDumpOE=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".AorB.sorted.addOE.xls"
	split2section=outdir + samplename + "_chr" + str(i) + "_" + binsize + ".sections.matrix"
	dictvalue={}
	listnumber=[]
	with open(addAorBsortmatchDumpOE) as addAorBsortmatchDumpOE, open(split2section,'w') as split2section:
		for eachline in addAorBsortmatchDumpOE:
			line=eachline.strip().split()
			if line[2]!="NaN":
				if int(line[0]) not in listnumber:
					listnumber.append(int(line[0]))
				if int(line[1]) not in listnumber:
					listnumber.append(int(line[1]))
				key1=line[0]+":"+line[1]
				key2=line[1]+":"+line[0]
				dictvalue[key1]=line[2]
				dictvalue[key2]=line[2]
		listnumber.sort()
		length=len(listnumber)
		sections=length//49
		dict_sections={}
		for i in range(0,50):
			for j in range(0,50):
				dict_sections[str(i)+":"+str(j)]=[0,0]
		for i in range(0,length):
			row=i//sections
			for j in range(0,length):
				col=j//sections
				key=str(listnumber[i])+":"+str(listnumber[j])	
				if row > 49:
					row=49
				if col > 49:
					col=49
				new_key=str(row)+":"+str(col)
				if key in dictvalue:
					if new_key in dict_sections:
						dict_sections[new_key][0]+=float(dictvalue[key])
						dict_sections[new_key][1]+=1
		for i in dict_sections:
			if dict_sections[i][1] != 0:
				split2section.write(i+"\t"+str(dict_sections[i][0]/dict_sections[i][1])+"\n")
			if dict_sections[i][1] == 0:
				split2section.write(i+"\t"+"NA"+"\n")

	del dictvalue;listnumber;dict_sections
	addAorBsortmatchDumpOE.close()
	split2section.close()

def saddleMatrixTidy(binsize,samplename,outdir):
	allsaddlematrix=outdir +"all_"+samplename + "_" + binsize + ".sections.matrix"
	allsaddlematrixTidy=outdir +"all_"+samplename + "_" + binsize + ".sections.matrix.tidy"
	dictmerge={}
	with open(allsaddlematrix) as allsaddlematrix, open(allsaddlematrixTidy,'w') as allsaddlematrixTidy:
		for eachline in allsaddlematrix:
			line=eachline.strip().split()
			if line[1]!="NA":
				key=line[0]
				if key in dictmerge:
					dictmerge[key][0]+=float(line[1])
					dictmerge[key][1]+=1
				if key not in dictmerge:
					dictmerge[key]=[float(line[1]),1]
		for i in range(0,50):
			w=''
			for j in range(0,50):
				if str(i)+":"+str(j) not in dictmerge or dictmerge[str(i)+":"+str(j)][1] < 5 :
					w=w+"NA"+"\t"
				else: #dictmerge[str(i)+":"+str(j)][1] !=0 :
					w=w+str(dictmerge[str(i)+":"+str(j)][0]/dictmerge[str(i)+":"+str(j)][1])+"\t"
			w=w.strip("\t")+"\n"
			allsaddlematrixTidy.write(w)
	del dictmerge
	allsaddlematrix.close()
	allsaddlematrixTidy.close()
def saddle(binsize,samplename,sampleref,outdir):
	print(sampleref,samplename)
	if sampleref=="control":	
		for i in range(1,24):
			if i==23:
				i="X"
				sort_EV1(outdir,samplename,binsize,i)
				dumpOEmatchEV1sortref(outdir,samplename,binsize,i)
				saddleMatrix(outdir,samplename,binsize,i)
			else:
				sort_EV1(outdir,samplename,binsize,i)
				dumpOEmatchEV1sortref(outdir,samplename,binsize,i)
				saddleMatrix(outdir,samplename,binsize,i)	
	else:
		for i in range(1,24):
			if i==23:
				i="X"
				dumpOEmatchEV1sort(outdir,samplename,binsize,i,sampleref)
				saddleMatrix(outdir,samplename,binsize,i)
			else:
				dumpOEmatchEV1sort(outdir,samplename,binsize,i,sampleref)
				saddleMatrix(outdir,samplename,binsize,i)	
	command=' '.join(["cat",outdir + samplename + "_chr*" + "_" + binsize + ".sections.matrix",'>',outdir +"all_"+samplename + "_" + binsize + ".sections.matrix"])
	os.system(command)
	saddleMatrixTidy(binsize,samplename,outdir)
	command=" ".join(["saddle_plot.R","--input",outdir +"all_"+samplename + "_" + binsize + ".sections.matrix.tidy","--output",outdir +"all_"+samplename + "_" + binsize + ".saddle.pdf"])
	os.system(command)	

	return

def top20percentEV1(outdir,samplename,binsize):
	dict_EV_A={}
	dict_EV_B={}
	dict_all_pos={}
	allAorB=outdir + "all_" + samplename + "_" + binsize + ".AorB.xls"
	top20AorB=outdir + "top20_" + samplename + "_" + binsize + ".AorB.xls"
	with open(allAorB) as allAorB, open(top20AorB,'w') as top20AorB:
		for eachline in allAorB:
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
				top20AorB.write(dict_all_pos[key]+'_'+'A'+'\n')
		for i in dict_EV_B:
			for n in range(len(dict_EV_B[i])-int(len(dict_EV_B[i])*0.2),len(dict_EV_B[i]),1):
				key=dict_EV_B[i][n]
				top20AorB.write(dict_all_pos[key]+'_'+'B'+'\n')

	allAorB.close();top20AorB.close()							
	del dict_EV_A;dict_EV_B;dict_all_pos
	
def top20percentEV1dump(outdir,samplename,binsize):
	top20percentEV1matchdump="dump/OE_250K/" + "all_"+samplename+"_"+binsize+".addChr.xls"
	top20AorB=outdir + "top20_" + samplename + "_" + binsize + ".AorB.xls"
	compartmentStrength=outdir + samplename + "_" + binsize + ".compartmentStrength.txt"
	EVa=[];EVb=[];chro={}
	with open(top20percentEV1matchdump) as top20percentEV1matchdump, open(top20AorB) as top20AorB, open(compartmentStrength,'w') as compartmentStrength:
		for eachline in top20AorB:
			line=eachline.strip().split('_')
			if line[-1]=="A":
				EVa.append(line[0]+'_'+line[1])
			if line[-1]=="B":
				EVb.append(line[0]+'_'+line[1])
		for eachline in top20percentEV1matchdump:
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
		#	print(chro[i][0],chro[i][1],chro[i][2],chro[i][3])
			s1=median(chro[i][0])+median(chro[i][1])
			if chro[i][2]!=[] and chro[i][3]!=[]:
				s2=median(chro[i][2])+median(chro[i][3])
				compartmentStrength.write(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2)+"\n")
			elif chro[i][2]!=[] and chro[i][3]==[]:
				s2=2*median(chro[i][2])
				compartmentStrength.write(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2)+"\n")
			elif chro[i][2]==[] and chro[i][3]!=[]:
				s2=2*median(chro[i][3])
				compartmentStrength.write(i+'\t'+str(s1/s2)+'\t'+str(s1)+'\t'+str(s2)+"\n")
			
	top20percentEV1matchdump.close();top20AorB.close();compartmentStrength.close()
	del EVa;EVb;chro

def strength(outdir,samplename,binsize):
	command = ' '.join(['cat',outdir + samplename + "_chr*" + "_" + binsize + ".AorB.xls",">",outdir + "all_" + samplename + "_" + binsize + ".AorB.xls"])
	os.system(command)
	top20percentEV1(outdir,samplename,binsize)
	top20percentEV1dump(outdir,samplename,binsize)	

#def 
