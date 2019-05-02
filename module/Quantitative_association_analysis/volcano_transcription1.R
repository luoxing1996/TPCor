#Args[6]=input Args[7]=output  Args[8]=fold Args[9]=pvalue

library(ggplot2)
Args <- commandArgs()
a<-as.numeric(Args[8])
b<-as.numeric(Args[9])
data =read.table(Args[6],header=T,row.names=1)
r0 = ggplot(data,aes(transcription_log2FC,-1*log10(transcription_FDR)),cex.axis=50,cex.lab=50,cex.main=50)
r1=r0+theme_bw()+theme(panel.grid=element_blank(),panel.border=element_blank(),axis.line=element_line(size=1,colour="black"))
r2 =r1+ geom_point(aes(color =transcription_type))
r3 = r2 +geom_point(aes(color =transcription_type)) 
r4=r3 + labs(title="transcription",x="log2(ratio)",y="-log10(P_value)")+theme(title=element_text(family="myFont",size=20,
                           face="italic",hjust=0.2,lineheight=0.2))+theme(axis.text.x=element_text(size=15))+theme(axis.text.y=element_text(size=15))

r5 = r4 +scale_color_manual(values = c("#00ba38","#619cff","#89A1B2","#f8766d"))
r6=r5+geom_hline(yintercept=-1*log(base=10,b),linetype=4)+geom_vline(xintercept=c(-a,a),linetype=4)

ggsave(Args[7],r6,width=8,height=8)