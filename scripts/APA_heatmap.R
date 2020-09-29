#!/usr/users/szhang3/Software/R-3.6.1/bin/Rscript 

library(optparse)
library(RColorBrewer)
library(gplots)
library(plot3D)

option_list <- list(
    make_option("--input", action = "store", type = "character"),
	make_option("--output", action = "store", type = "character")
    )
opt <- parse_args(OptionParser(option_list=option_list))

par(font.main=2, font.sub=1, font.lab=1,font.axis=1, cex.main=0.8, cex.sub=0.8, cex.lab=0.9, cex.axis=0.9,lab=c(8,8,0), mgp=c(1.5,0.6,0),bty="l",las=1)

pdf(opt$output)
#hmbreaks = c(seq(0, 1, length=101))

APA  = as.matrix(read.table(opt$input,head=FALSE,sep="\t"))

myColors <- colorRampPalette(c("white","red"))(100)

valueVec = as.numeric(APA[APA>0])
valueVec = valueVec[!is.na(valueVec)]
minVp = min(valueVec)
maxVp = max(valueVec)

for(i in 1:nrow(APA)){
for(j in 1:ncol(APA)){
	{ APA[i,j] = 2*((APA[i,j] - minVp) / (maxVp - minVp))
} } }

heatmap.2(APA,Rowv = FALSE,Colv= FALSE, dendrogram="none", scale = "none", revC = FALSE, density.info="none", col=myColors, symm = TRUE, keysize=2, sepwidth = c(0,0), sepcolor="black",trace="none")

dev.off()
