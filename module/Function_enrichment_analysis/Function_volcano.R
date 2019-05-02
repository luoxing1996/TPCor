#Args[6]=input Args[7]=output
.libPaths( "/zfssz3/SP_MSI/Pipeline/software/R/R-devel/lib64/R/library" );
library(ggplot2)
Args <- commandArgs()
data =read.table(Args[6],header=T)
r0 = ggplot(data,aes(-1*log10(protein_P_value),-1*log10(transcription_P_value)))
r1=r0+theme_bw()+theme(panel.grid=element_blank(),panel.border=element_blank(),axis.line=element_line(size=1,colour="black"))
r2 =r1+ geom_point(aes(color =significance),cex=4)+xlim(0,4)+ylim(0,4)
r3=r2 + labs(title=Args[8],x="Protein_log10(-P_value)",y="Transcription_log10(-P_value)",cex.main=20)+theme(title=element_text(family="myFont",size=20,
                           face="italic",hjust=0.2,lineheight=0.2))+theme(axis.text.x=element_text(size=20))+theme(axis.text.y=element_text(size=20))
r4 = r3 +scale_color_manual(values = c("#f8766d","#619cff","#00ba38"))
r5=r4+geom_hline(yintercept=1.3,linetype=4)+geom_vline(xintercept=1.3,linetype=4)
ggsave(Args[7],r5,width=10,height=10)
