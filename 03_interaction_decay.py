#!/bin/python

import sys
import os

scripts="./scripts/"
binsize=sys.argv[1]
Type=sys.argv[2]
command="mkdir -p Interaction_decay"
os.system(command)

def interaction_decay():
	if Type=="one":
		No="none"
	elif Type=="two":
		infile1=sys.argv[3]
		infile2=sys.argv[4]
		command=" ".join(["python",scripts+"distancebin.py",infile1,"Interaction_decay/"+"file1_"+str(binsize)+".distancebin",str(binsize)])
		os.system(command)
		command=" ".join(["python",scripts+"distancebin.py",infile2,"Interaction_decay/"+"file2_"+str(binsize)+".distancebin",str(binsize)])
		os.system(command)
		command=" ".join([scripts+"distancebin_2sample.R","Interaction_decay/"+"file1_"+str(binsize)+".distancebin","Interaction_decay/"+"file2_"+str(binsize)+".distancebin",str(binsize),"Interaction_decay/Interaction_decay."+str(binsize)+".pdf"])
		os.system(command)
	elif Type=="multiple":
		No="none"

	return

interaction_decay()
