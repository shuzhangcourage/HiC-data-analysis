#!/bin/bash

# Slurm Parameters
#SBATCH -p fat 
#SBATCH --job-name=APA
#SBATCH --output=APA.%A_%a.out
#SBATCH --error=APA.%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=100gb
#SBATCH --time=1:00:00

#java -Djava.awt.headless=true -Xmx32000m -jar juicer_tools_1.13.02.jar apa  -c 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X \
-r 10000 -k KR -q 3 -w 6 -n 15 -u inter_30.hic loops.txt APA/control

awk '$5-$2>150000 || $5-$2<-150000' loops.txt | wc -l 
python scripts/APA_average.py APA/control/10000/gw/APA.txt APA/control/10000/gw/APA.average 3785 ##18.334315060498376
python scripts/APA_average_tidy2heatmap.py APA/control/10000/gw/APA.average APA/control/10000/gw/APA.heatmap
./scripts/APA_heatmap.R --input APA/degron/10000/gw/APA.heatmap --output APA/degron/10000/gw/APA.heatmap.pdf
