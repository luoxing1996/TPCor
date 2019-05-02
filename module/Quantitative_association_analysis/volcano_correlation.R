#Args[6]=input Args[7]=output

library(ggplot2)
Args <- commandArgs()
data =read.table(Args[6],header=T,row.names=1)
r0 = ggplot(data,aes(log10_C_Expression,log10_T_Expression))
r1=r0+theme_bw()+theme(panel.grid=element_blank(),panel.border=element_blank(),axis.line=element_line(size=1,colour="black"))
r2 =r1+ geom_point(aes(color =Gene_group))
r3 = r2 +geom_point(aes(color =Gene_group)) 
r4=r3 + labs(title="Relationship between associated genes and non-associated genes",x="log10_(C-Expression)",y="log10_(T-Expression)")+theme(title=element_text(family="myFont",size=15,
                           face="italic",hjust=0.2,lineheight=0.2))+theme(axis.text.x=element_text(size=15))+theme(axis.text.y=element_text(size=15))
r5 = r4 +scale_color_manual(values = c("#619cff","#f8766d"))

ggsave(Args[7],r5,width=8,height=8)
