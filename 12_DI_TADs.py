#!/bin/python

import sys
import os

genomesize="chrom.sizes.hg38.filter" 
scripts="./scripts/"
centromere="hg38_centro_telemere_selected"
dump=sys.argv[1]#path of dump_value
name=sys.argv[2]#name of samples
binsize=sys.argv[3]#binsize
region=sys.argv[4]#upstream and downstream

command="mkdir -p DI_TADs"
os.system(command)

def DI():
	command=" ".join(["python",scripts+"DI_TADs.py",genomesize,dump+"all_"+name+".addChr.xls","DI_TADs/"+name+"_"+binsize+".DI",binsize,region])
	os.system(command)
	command=" ".join(['sed "s/X/23/g"',"DI_TADs/"+name+"_"+binsize+".DI", ">" ,"DI_TADs/"+name+"_"+binsize+".DI.DI"])
	os.system(command)
	return

def hmm():
	command = " ".join(['sed "s/inputname/'+"DI_TADs\/"+name+"_"+binsize+".DI.DI"+'/g"',scripts+"domain_calling.m","|",'sed "s/outputname/'+"DI_TADs\/"+name+"_"+binsize+".hmm"+'/g"',">",scripts+name+binsize+"domain_calling.m"])
	os.system(command)
	command=" ".join(["nice matlab <",scripts+name+binsize+"domain_calling.m"])
	os.system(command)
	command="rm -f "+scripts+name+binsize+"domain_calling.m"
	os.system(command)
	return

#def tidy():
#	command=" ".join([" file_ends_cleaner.pl","DI_TADs/"+name+"_"+binsize+".hmm","DI_TADs/"+name+"_"+binsize+".DI.DI","|"," converter_7col.pl",">","DI_TADs/"+name+"_"+binsize+".hmm_7colfile"])
#	os.system(command)
#	for i in range(1,24):
#		command=" ".join(["awk","'$1=="+'"chr'+str(i)+"\"'","DI_TADs/"+name+"_"+binsize+".hmm_7colfile",">", "DI_TADs/"+name+"_"+binsize+".hmm_7colfile"+".chr"+str(i)])
#		os.system(command)		
		#command=" ".join(["ls","DI_TADs/"name+"_"+binsize+".hmm_7colfile"+".chr"+str(i),"|","while read line; do hmm_probablity_correcter.pl $line 2 0.99",binsize,"| hmm-state_caller.pl",genomesize,"chr"+str(i),"| hmm-state_domains.pl > $line.finaldomaincalls; done"])
		#command="ls "+"DI_TADs/"name+"_"+binsize+".hmm_7colfile"+".chr"+str(i)+" | while read line; do hmm_probablity_correcter.pl $line 2 0.99 "+ str(binsize)+" | hmm-state_caller.pl "+genomesize+" chr"+str(i)+" | hmm-state_domains.pl > $line.finaldomaincalls; done"
		#print(command)
		#os.system(command)
#for i in {1..23}; do ls *10000.hmm_7colfile.chr${i} | while read line ; do  hmm_probablity_correcter.pl $line 2 0.99 10000 | hmm-state_caller.pl ~/Juicer/references/chrom.sizes.hg38.filter chr${i} |  hmm-state_domains.pl > $line.finaldomaincalls; done ; done
#
#		tmp=open("tmp"+name+binsize+".sh","w")
#		tmp.write(command+"\n")
#		command=" ".join(["sh","tmp"+name+binsize+".sh"])
#		os.system(command)
		#command=" ".join(["rm -f ","tmp"+name+binsize+".sh"])
		#os.system(command)
#		command=" ".join(["python",scripts+"DIhmm2JuicerBedpe.py","DI_TADs/"+name+"_"+binsize+".hmm_7colfile"+".chr"+str(i)+".finaldomaincalls","DI_TADs/"+name+"_"+binsize+".hmm_7colfile"+".chr"+str(i)+".finaldomaincalls.bedpe"])
#		os.system(command)	
#	command=" ".join(["cat","DI_TADs/"+name+"_"+binsize+".hmm_7colfile"+".chr*.finaldomaincalls.bedpe",">","DI_TADs/all_"+name+"_"+binsize+".hmm_7colfile"+".finaldomaincalls.bedpe"])
#	os.system(command)
#	command=" ".join(["awk '$3-$2>=150000'","DI_TADs/all_"+name+"_"+binsize+".hmm_7colfile"+".finaldomaincalls.bedpe",">","DI_TADs/all_"+name+"_"+binsize+".hmm_7colfile"+".finaldomaincalls.bedpe.filter_150K"])
#	os.system(command)
#	command=" ".join(["python",scripts+"TADs_rm_centro.py","DI_TADs/all_"+name+"_"+binsize+".hmm_7colfile"+".finaldomaincalls.bedpe.filter_150K",centromere,name+"_"+binsize+".hmm_7colfile"+".finaldomaincalls.bedpe.filter_150K.filtercentromere"])
#	os.system(command)
#	return

	
DI()
hmm()
#tidy()
#command = 'ls DI_TADs/degron_25000.hmm_7colfile.chr1 | while read line; do hmm_probablity_correcter.pl $line 2 0.99 25000 |  hmm-state_caller.pl /usr/users/szhang3/Juicer/references/chrom.sizes.hg38.filter chr1 |  hmm-state_domains.pl > $line.finaldomaincalls ;done'
#os.system(command)
