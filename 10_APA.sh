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

# Commands
# sbatch 10_APA.sh
# squeue -u szhang3
# scancel 

#java -Djava.awt.headless=true -Xmx32000m -jar /usr/users/szhang3/Juicer/scripts/juicer_tools_1.13.02.jar apa  -c 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X -r 10000 -k KR -q 3 -w 6 -n 15 -u /usr/users/szhang3/Project/TOP2A2B/Data/01_AKI84_A006850084/TOP2A2B_control_merge/inter_30.hic /usr/users/szhang3/Project/TOP2A2B/Code/2_Annotation/SIP_Loop/control_10K_fdr005/loops.txt APA/control
#java -Djava.awt.headless=true -Xmx32000m -jar /usr/users/szhang3/Juicer/scripts/juicer_tools_1.13.02.jar apa  -c 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X -r 10000 -k KR -q 3 -w 6 -n 15 -u /usr/users/szhang3/Project/TOP2A2B/Data/01_AKI84_A006850084/TOP2A2B_degron_merge/inter_30.hic /usr/users/szhang3/Project/TOP2A2B/Code/2_Annotation/SIP_Loop/degron_10K_fdr005/loops.txt APA/degron

awk '$5-$2>150000 || $5-$2<-150000' /usr/users/szhang3/Project/TOP2A2B/Code/2_Annotation/SIP_Loop/control_10K_fdr005/loops.txt | wc -l 
awk '$5-$2>150000 || $5-$2<-150000' /usr/users/szhang3/Project/TOP2A2B/Code/2_Annotation/SIP_Loop/degron_10K_fdr005/loops.txt | wc -l 
python scripts/APA_average.py APA/control/10000/gw/APA.txt APA/control/10000/gw/APA.average 3785 ##18.334315060498376
python scripts/APA_average.py APA/degron/10000/gw/APA.txt APA/degron/10000/gw/APA.average 3662 ##18.711879931662917
python scripts/APA_average_tidy2heatmap.py APA/control/10000/gw/APA.average APA/control/10000/gw/APA.heatmap
python scripts/APA_average_tidy2heatmap.py APA/degron/10000/gw/APA.average APA/degron/10000/gw/APA.heatmap

./scripts/APA_heatmap.R --input APA/degron/10000/gw/APA.heatmap --output APA/degron/10000/gw/APA.heatmap.pdf
./scripts/APA_heatmap.R --input APA/control/10000/gw/APA.heatmap --output APA/control/10000/gw/APA.heatmap.pdf
