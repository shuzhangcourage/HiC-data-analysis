#!/bin/python

import sys
import os

Script="./scripts/"
EV1="./EV1/EV1_250K/"
dump="./dump/OE_250K/"
name=sys.argv[1]# name of sample
reference=sys.argv[2]# if reference
binsize="250000" # default

def saddle():
	if reference=="reference":	
		for i in range(1,24):
			if i==23:
				i="X"
				script1=Script+"sort_EV1.py"
				infile=EV1+name+"_chr"+str(i)+"_"+binsize+".AorB.xls"
				outfile=EV1+reference+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				command=" ".join(["python", script1, infile, outfile])
	#			print(command)
				os.system(command) # EV1 sorting
				script2=Script+"sort_dumpOE250.py" 
				infile1=EV1+reference+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				infile2=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				command=" ".join(["python", script2, infile1, infile2, outfile])	
	#			print(command)
				os.system(command)	# dumpOE sorting
				script3=Script+"saddle_matrix.py"
				infile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".50section.matrix"
				command=" ".join(["python", script3, infile, outfile])
	#			print(command)
				os.system(command)	
			else:
				script1=Script+"sort_EV1.py"
				infile=EV1+name+"_chr"+str(i)+"_"+binsize+".AorB.xls"
				outfile=EV1+reference+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				command=" ".join(["python", script1, infile, outfile])
	#			print(command)
				os.system(command) # EV1 sorting
				script2=Script+"sort_dumpOE250.py" 
				infile1=EV1+reference+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				infile2=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				command=" ".join(["python", script2, infile1, infile2, outfile])	
	#			print(command)
				os.system(command)	# dumpOE sorting
				script3=Script+"saddle_matrix.py"
				infile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".50section.matrix"
				command=" ".join(["python", script3, infile, outfile])
	#			print(command)
				os.system(command) #generate 50sections for saddle plot
	
	else:
		for i in range(1,24):
			if i==23:
				i="X"
				script2=Script+"sort_dumpOE250.py" 
				infile1=EV1+"reference"+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				infile2=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				command=" ".join(["python", script2, infile1, infile2, outfile])	
	#			print(command)
				os.system(command)	# dumpOE sorting
				script3=Script+"saddle_matrix.py"
				infile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".50section.matrix"
				command=" ".join(["python", script3, infile, outfile])
	#			print(command)
				os.system(command)
			else:
				script2=Script+"sort_dumpOE250.py" 
				infile1=EV1+"reference"+"_chr"+str(i)+"_"+binsize+".AorB.sort.xls"
				infile2=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				command=" ".join(["python", script2, infile1, infile2, outfile])	
	#			print(command)
				os.system(command)	# dumpOE sorting
				script3=Script+"saddle_matrix.py"
				infile=dump+name+"_chr"+str(i)+"_"+binsize+".addChr.sort.xls"
				outfile=dump+name+"_chr"+str(i)+"_"+binsize+".50section.matrix"
				command=" ".join(["python", script3, infile, outfile])
	#			print(command)
				os.system(command) #generate 50sections for saddle plot
	
	command="cat "+dump+name+"_chr*.50section.matrix > "+dump+"all_"+name+".50section.matrix"
	os.system(command)
	command=" ".join(["python",Script+"saddle_matrix_tidy.py",dump+"all_"+name+".50section.matrix","all_"+name+".50section.matrix.tidy"])
	os.system(command)
	command=" ".join([Script+"saddle_plot.R","--input","all_"+name+".50section.matrix.tidy","--output",name+"_"+binsize+"_"+"saddlePlot.pdf"])
	os.system(command)	

	return

def strength():
	command=" ".join(["python",Script+"top20percent_EV1.py",EV1+"all_"+name+"_"+binsize+".AorB.xls",EV1+"top20percent_"+name+"_"+binsize+".AorB.xls"])
	os.system(command)
	command=" ".join(["python",Script+"compartment_strength.py",dump+"all_"+name+"_"+binsize+".addChr.xls",EV1+"top20percent_"+name+"_"+binsize+".AorB.xls",">",name+"_"+binsize+"strength_value.txt"])
	os.system(command)	
	return

saddle()
strength()
