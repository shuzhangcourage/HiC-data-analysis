#!/bin/Rscript
args <- commandArgs(trailingOnly=TRUE)
file1=read.table(args[1],head=FALSE)
file2=read.table(args[2],head=FALSE)
binsize=as.integer(args[3])
out=args[4]
pdf(out)

layout(matrix(c(1,2,3,4),nr=2, byrow=T))
par(font.main=2, font.sub=1, font.lab=1,font.axis=1, cex.main=1, cex.sub=1, cex.lab=1, cex.axis=1,lab=c(8,8,0), mgp=c(1.8,0.6,0),bty="l",las=1)


plot(log10(file1$V1*binsize), log10(file1$V2/sum(file1$V2)), ylim=c(-8,-1),xlim=c(4,8.5),type='l', col='blue',cex=1, xlab="contact distance (log10 bp)", ylab="interaction frequency (log10)", sub="blue is control;red is degron")
lines(log10(file2$V1*binsize), log10(file2$V2/sum(file2$V2)), col='red',cex=1)

dev.off()
