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
#SBATCH --array=1-14

# Commands
# sbatch 01_dump.sh
# squeue -u szhang3
# scancel 5349837

# Input
inputFileName="./input/Dump_input_parameters.txt"
parameters=`sed "${SLURM_ARRAY_TASK_ID}q;d" $inputFileName`

# extracting matrix
time python ./01_dump.py $parameters
