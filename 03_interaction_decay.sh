#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=interaction_decay
#SBATCH --output=interaction_decay.%A_%a.out
#SBATCH --error=interaction_decay.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=50gb
#SBATCH --time=1:00:00


time python ./03_interaction_decay.py 10000 two dump/OB_10K/file1.xls dump/OB_10K/file2.xls
