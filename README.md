# TPCor
intergrated approach of the transcriptome and proteome 
step：
1.根据时间和项目号，任务单号在你的工作目录中创建一个为项目号的文件夹（以下统称该文件夹为root）。
2.拷贝/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/bin文件下的run.sh和correlation_config.json到root。
3.根据项目内容，修改相应的correlation_config.json内的参数。
4.将RNA_Seq所有比较组文件夹拷贝到你的目录中命名为trans（以下统称该文件夹为transcription_root）。
5.将iTRAQ所有比较组文件夹拷贝到你的目录中命名为pro（以下统称该文件夹为protein_root）。
6.将protein_root中的对应的比较组根据json文件的Comparison_Group参数设置对应的文件名，注意每个比较组需要_C.xls，_F.xls，_P.xls，_path.xls，_Down.xls，_Up.xls,.xls。
7.将transcription_root中的对应的比较组根据json文件的Comparison_Group参数设置对应的文件名，注意每个比较组需要_C.txt，_F.txt，_P.txt，_path.txt，C-VS-T.基因DiffExp.xls，如果转录组id为基因，则需要相应的参考基因集文件refMrna.fa和id转换文件基因2tr，如果Whether the transcriptome ko file exist参数为yes，则需要对应的.ko文件。
8.shrun.sh即可。
注意：如果输出BGIsmile,则运行成功，否则失败，找到原因后，设置json文件的step从对应步骤开始即可，如果2-6步运行时间超过一小时，则很可能运行失败，你需要检测配置错误，重新从该步运行。json中的Comparison_Group参数命名的id可以是任意id，但是必须要与TP_Cor所对应的比较组命名一致。转录因子流程需要你查阅附件1中看是否有该物种再决定是否进行转录因子分析。转录组需要提供相应的ko文件，如果找不到ko文件，可以将Whether the transcriptome ko file exist设置为no，流程会再跑一遍转录组的Pathway通路富集流程。如果转录组蛋白质组没有做相应的注释与富集，可以设置相应参数为no，该流程会自动进行注释与富集，并且会生成相应的ko文件。
