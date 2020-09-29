#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=dump
#SBATCH --output=dump.%A_%a.out
#SBATCH --error=dump.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=50gb
#SBATCH --time=1:00:00
#SBATCH --array=1-2


inputFileName="./input/Dump_input_parameters.txt"
parameters=`sed "${SLURM_ARRAY_TASK_ID}q;d" $inputFileName`

time python ./01_dump.py $parameters
