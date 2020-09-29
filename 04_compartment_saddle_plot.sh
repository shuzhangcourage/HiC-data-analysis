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


#time python ./04_compartment_saddle_plot.py control reference 
