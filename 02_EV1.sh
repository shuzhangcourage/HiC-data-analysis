#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=EV1
#SBATCH --output=EV1.%A_%a.out
#SBATCH --error=EV1.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=50gb
#SBATCH --time=2:00:00
#SBATCH --array=1-7

# Commands
# sbatch 02_EV1.sh
# squeue -u szhang3
# scancel 5350087

# Input
inputFileName="/usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/input/EV1_input_parameters.txt"
parameters=`sed "${SLURM_ARRAY_TASK_ID}q;d" $inputFileName`

# extracting matrix
time python /usr/users/szhang3/Project/Papantonis_Pol2Degron/Code/3_Annotation_pipline/02_EV1.py $parameters

