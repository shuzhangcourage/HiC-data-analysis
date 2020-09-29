#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=DI_TADs
#SBATCH --output=DI_TADs.%A_%a.out
#SBATCH --error=DI_TADs.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100gb
#SBATCH --time=1:00:00

# Commands
# sbatch 04_DI_TADs.sh
# squeue -u szhang3
# scancel 


# extracting matrix
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/03_interaction_decay.py 10000 two dump/OB_10K/all_reenter_merge_control_10000.addChr.xls dump/OB_10K/all_reenter_degron_10000.addChr.xls  

