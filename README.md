# TPCor
intergrated approach of the transcriptome and proteome 
Step:
1. According to the time and project number, the task ticket number creates a folder with the project number in your working directory (hereinafter referred to as the folder as root).

2. Copy run.sh and correlation_config.json from the /ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/bin file to root.

3. Modify the parameters in the corresponding correlation_config.json according to the project content.

4. Copy all the comparison group folders of RNA_Seq to your directory and name it trans (hereinafter referred to as the folder for transcription_root).

5. Copy all the iTRAQ comparison group folders to your directory and name them pro (hereinafter referred to as the folder protein_root).

6. Set the corresponding comparison group in the protein_root to the corresponding file name according to the Comparison_Group parameter of the json file. Note that each comparison group requires _C.xls, _F.xls, _P.xls, _path.xls, _Down.xls, _Up .xls, .xls.

7. Set the corresponding comparison group in the transcription_root to the corresponding file name according to the Comparison_Group parameter of the json file. Note that each comparison group requires _C.txt, _F.txt, _P.txt, _path.txt, C-VS-T. Gene DiffExp.xls, if the transcript id is a gene, the corresponding reference gene set file refMrna.fa and id conversion file gene 2tr are required. If the Which the transcriptome ko file exist parameter is yes, the corresponding .ko file is required.

8. sh run.sh 

Note: If BGIsmile is output, the operation is successful, otherwise it fails. After finding the reason, the step of setting the json file can start from the corresponding step. If the running time of 2-6 steps exceeds one hour, it is likely to fail. You need to detect the configuration. Error, re-run from this step. The id named by the Comparison_Group parameter in json can be any id, but it must be the same as the comparison group corresponding to TP_Cor. The transcription factor process requires you to look at Annex 1 to see if there is a species to decide whether or not to perform a transcription factor analysis. The transcriptome needs to provide the corresponding ko file. If the ko file is not found, you can set the the transcriptome ko file exist to no, and the process will run the Pathway path enrichment process of the transcript. If the transcriptome proteome is not commented and enriched, you can set the corresponding parameter to no, the process will automatically annotate and enrich, and the corresponding ko file will be generated.
