#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=saddle
#SBATCH --output=saddle.%A_%a.out
#SBATCH --error=saddle.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100gb
#SBATCH --time=2:00:00

# Commands
# sbatch 04_compartment_saddle_plot.sh
# squeue -u szhang3
# scancel 

# extracting matrix
#time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py reenter_merge_control reference 
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py 14hG1_control non_reference
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py 14hG1_degron non_reference
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py 14hG1_Tri non_reference
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py reenter_degron non_reference
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py 2h_async_degron non_reference
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/04_compartment_saddle_plot.py 2h_async_control non_reference


