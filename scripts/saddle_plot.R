#!/usr/users/szhang3/Software/R-3.6.1/bin/Rscript 

library(optparse)
library(RColorBrewer)
library(gplots)

option_list <- list(
    make_option("--input", action = "store", type = "character"),
	make_option("--output", action = "store", type = "character")
    )
opt <- parse_args(OptionParser(option_list=option_list))

layout(matrix(c(1,2,3,4),nr=2, byrow=T))
par(font.main=2, font.sub=1, font.lab=1,font.axis=1, cex.main=1, cex.sub=1, cex.lab=1, cex.axis=1,lab=c(8,8,0), mgp=c(1.8,0.6,0),bty="l",las=1)

pdf(opt$output)

saddle  = as.matrix(read.table(opt$input,head=FALSE,sep="\t"))
#max = as.matrix(read.table(opt$max,head=FALSE,sep="\t"))

myColors <- colorRampPalette(c("steelblue","white","tomato"))(100)

valueVec = as.numeric(saddle[saddle>0])
valueVec = valueVec[!is.na(valueVec)]
minVp = min(valueVec)
maxVp = max(valueVec)

maxRange=2
minRange=0.5

if (maxVp >= maxRange){
for(i in 1:nrow(saddle)){
for(j in 1:ncol(saddle)){
if(saddle[i,j] >= maxRange){
saddle[i,j] = maxRange}	} } }

if (minVp<=minRange){
for(i in 1:nrow(saddle)){
for(j in 1:ncol(saddle)){
if(saddle[i,j] <= minRange){
saddle[i,j] = minRange} } } }

if (maxVp < maxRange){
for(i in 1:nrow(saddle)){
for(j in 1:ncol(saddle)){
if(saddle[i,j] == maxVp){
saddle[i,j] = maxRange} } } }

if (minVp > minRange){
for(i in 1:nrow(saddle)){
for(j in 1:ncol(saddle)){
if(saddle[i,j] == minVp){
saddle[i,j] = minRange} } } }

saddle=log2(saddle)


heatmap.2(saddle,Rowv = FALSE,Colv= FALSE, dendrogram="none", scale = "none", revC = FALSE, density.info="density", denscol="green", trace="none",col=myColors,symm = TRUE,symbreaks=TRUE,key.title="Color Key", key.xlab="log2(obs/exp)",key.ylab="value density",main="Saddle Plot", xlab="EV1 from negtive --> positive", ylab="EV1 from positive --> negtive")

dev.off()
