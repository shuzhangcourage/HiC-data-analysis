#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=SIP
#SBATCH --output=SIP.%A_%a.out
#SBATCH --error=SIP.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100gb
#SBATCH --time=20:00:00
#SBATCH --array=1-2

# Input
inputFileName="./input/SIP_Loop_input_parameters.txt"
parameters=`sed "${SLURM_ARRAY_TASK_ID}q;d" $inputFileName`

# Detecting Loops
time python ./09_SIP_Loop.py $parameters
