#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=DI_TADs
#SBATCH --output=DI_TADs.%A_%a.out
#SBATCH --error=DI_TADs.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100gb
#SBATCH --time=24:00:00

# Input
inputFileName="input/DI_TADs_input_parameters.txt"
parameters=`sed "${SLURM_ARRAY_TASK_ID}q;d" $inputFileName`

# extracting matrix
time python ./12_DI_TADs.py $parameters
