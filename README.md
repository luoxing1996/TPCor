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

：
.
├──bin#Running binary script

│├──correlation_config.json#Profile script

│└──run.sh#Run the script, pay attention to the python build environment and the software is compatible with various linux versions.

├──lib#library about database and Chinese transcoding file

│└──anaconda3#Python configuration environment, non-default, the program has been modified

│└──database#Plant transcription factor database and string database

│└──pdf#Pdf compiler

│└──head.png#PS head file

│└──map_title.tab#Personalized font

│└──wqy-microhei.ttc#Personalized font

├──module

│├───Blast#step 1 Sequence Alignment

││├──Blast_comparison.py#Step 1 Sequence Alignment script

││├──Blast_network.py#Network module Sequence Alignment script

││└──Blast_TF.py#Transcription factor module Sequence Alignment script

││└──Screening_comparison_results.pl#e_value modify dealing script

│	└───Quantitative_association_analysis#step 2 Quantitative module analysis

│├──heat.R

│├──Quantitative_correlation_map.py

│├──Quantitative_heat_map.py

│├──Quantitative_venn_map.py

│└──Quantitative_volcano_map.py

│└──volcano_correlation.R

│└──volcano_protein1.R

│└──volcano_protein2.R

│└──volcano_transcription1.R

│└──volcano_transcription2.R

│	└───Function_enrichment_analysis#step 3 Function analysis

│├──Function_all_ko_Integrated_analysis.py#All identified gene ko integration analysis

│├──Function_bubble_map.py#Function bubble map

│├──Function_correlation_map.py#Function correlation map

│├──Function_diff_ko_Integrated_analysis.py#Diff identified gene ko integration analysis

│├──Function_volcano_map.py#Function volcano scipt

│└──Function_volcano.R#Function volcano map

│	└───Interaction_network_association_analysis	

│├──network.py#python3 network script#step 4 network analysis

│├──Pathway_network.sh#Pathway network script

│├──PathwayNetwork-hyb.pl#Pathway network Tree and branches script

│├──PPI_fd_relation.py#Network weight analysis

│└──PPI_network.pl#PPI network script

│└──PPI_relation.py#PPI weight analysis

│	└───Transcription_factor_correlation_analysis	

│├──TF_all_map.py#The transcription factor script is a whole script, and the user can choose whether to perform transcription factor analysis.

├──src

│├──Associated_total_file_generation.py#step 0 associated_total_file_generation

│├──Fasta_sequence_extraction.py#step 0 extract fasta sequence and generate integrated file table

│├──File_creation_initialization.py#Upstream script compatibility handles files, creates all the fasta and configuration input files needed for the process, and creates a program structure directory

│├──Function_analysis_total_file_generation.py#step 3 all Function module Configuration file

│├──Function_Annotation_and_enrichment.py#step 1 Annotation and enrichment【optional】

│├──KO_file_processing.py#ko file processing

│├──main.py#main script about step 0-6 file dealing processing

│├──mRNA_and_protein_ko_combine.py#step 3 mRNA and protein ko combine file

│├──Network_deal_sh_generation.py#Network module Configuration file

│├──Network_process_file_creation.py#Network  module result Configuration file,including hidden network node analysis and tree and branch selection analysis

│├──pdf.sh# step 6 pdf report generation

│├──Submit_analysis_files_and_pdf_generation.py#step 6 pdf generation script

│├──help.pdf#User help document

└──demo#BGI Apple sample code, accessible only to administrators,


Bin: The main program and json file, usually only the main script that the user is allowed to use will be placed in this directory.

Lib: The environment variable information needed to run the process, the python third-party package, the UI diagram, the transcription factor plant database, and the required fonts for reporting.If necessary, please send an email luoxing@genomics.cn

Demo: A set of standard test data.

Module: software and scripts.

Src: All algorithms of the process, usually only accessible by administrators.

Tutorial: Help documentation.
