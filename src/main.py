3
�C�\8T  �               @   s�  d dl Z d dlZd dlZd dlZe j� Zedd�Zeje�Z	e	d d Z
e	d d Ze	d d Ze	d d Ze	d d	 Ze	d
 d Ze	d d Ze	d d Ze	d d Ze	d d Ze	d d Ze	d d Ze	d d Ze	d d Ze	d d Ze
jd�Ze j� jd�d Zdej� k�r eZndej� k�r2eZde Zdeef Zdeeeeeef Z d eeeef Z!d!eeeeeeeeeef
 Z"d"eeeeeeeeeeeeeeeef Z#d#eeeef Z$x$eD ]Z%e$d$e%eee%e%f 7 Z$�q�W d%eeeeeeeef Z&d&eeef Z'd'd(� Z(e)d)k�r�d Z*d*ek�rJe+e�Zed+k�r@d,Z*e(e� nTd*ek�r�ejd*�Z,x>e-e+e,d  �e+e,d, �d, �D ]Z.e.d+k�r�d,Z*e(e.� �q~W e*d,k�r��xe j/j0d-��r�e j1d.� d/Z2x�e2j� D ]�Z3g Z4x�e-d0d;d<�D ]�Z5g Z6d1Z7xte-d=d2�D ]fZ8e8d3 d4 e5d5 d4  d, d6 e8d3 d4 e5d5 d6   Z9e9d k�r\e7e3e8e:e3�  7 Z7ne7d77 Z7�q W e6j;e7� e4e67 Z4�q�W �q�W ejj<� j=d8�Z>e?d9e> � e?d:j@e4�� P �q�W dS )>�    Nzcorrelation_config.json�rZBasis_InformationZComparison_Groupz(Correlation analysis process server path�step�perl_HOME_PATH�SGEQueuezFilter ParametersZBlast_MemoryZPython_HOME_PATHZNetworkZNetworkMemoryZ
Annotationz'Whether the transcriptome ko file existzTranscription factorz+Whether to do transcription factor analysis�TF_Species_type�TF_plant_database�TF_animal_databasez5Whether to do transcriptome annotation and enrichmentz0Whether to do proteome annotation and enrichment�,�/�   ZanimalZplanta�  
Welcome %s to use the  BGI TP_Cor!
Computer language:python,c,shell,perl,R,html/css/javascript
version number:1.0
Item Number:test
author:heyanbin,luoxing,ningxiaolian,zhuyueqin
Development time:2018.11.20 to 2018.12.24
If you have any questions, please email:luoxing@genomics
The process will start running after 30s. Please check all parameter settings correctly. All the required files already exist. 
If you are not ready, please press ctrl+C to exit!
You can drink a glass of water ,wait it......
z/%spython %s/src/File_creation_initialization.pyz~
%spython %s/module/Blast/Blast_comparison.py
%spython %s/module/Blast/Blast_TF.py
%spython %s/module/Blast/Blast_network.py 
zZ

%spython %s/module/Blast/Blast_comparison.py
%spython %s/module/Blast/Blast_network.py 
a�  
%s/perl %smodule/Blast/Screening_comparison_results.pl blast_all.out blast_all_filter.out
%spython %s/src/Associated_total_file_generation.py
%spython %s/module/Quantitative_association_analysis/Quantitative_volcano_map.py
%spython %s/module/Quantitative_association_analysis/Quantitative_correlation_map.py
%spython %s/module/Quantitative_association_analysis/Quantitative_venn_map.py

a"  
%spython %s/src/Function_analysis_total_file_generation.py
%spython %s/module/Function_enrichment_analysis/Function_bubble_map.py
%spython %s/module/Function_enrichment_analysis/Function_correlation_map.py
%spython %s/src/KO_file_processing.py
%spython %s/src/mRNA_and_protein_ko_combine.py
%spython %s/module/Function_enrichment_analysis/Function_volcano_map.py
%spython %s/module/Function_enrichment_analysis/Function_all_ko_Integrated_analysis.py
%spython %s/module/Function_enrichment_analysis/Function_diff_ko_Integrated_analysis.py



    zf
%spython %s/src/Network_process_file_creation.py 
%spython %s/src/Network_deal_sh_generation.py     
z�sh %s_network.sh
%spython %s/module/Interaction_network_association_analysis/Network_ppi_filter.py ./Data_Analysis/%s/Network/
sh %s_network_filter.sh
a�    
%s/perl %smodule/Blast/Screening_comparison_results.pl TF_transcription_all_blast.out TF_transcription_blast_all_filter.out
%s/perl %smodule/Blast/Screening_comparison_results.pl TF_protein_all_blast.out TF_protein_blast_all_filter.out
for i in `ls %s/*xls`;do
awk -F'	' '{print $2"	"$(NF-1)"	"$NF}' $i;
done|sort|uniq|awk -F'	' 'NR==FNR{a[$1]=$0;next}{split($2,array,/:/);if (array[1] in a) print $1"	"a[array[1]];else if(array[2] in a)print $1"	"a[array[2]]}' - TF_transcription_blast_all_filter.out >>TF_transcription_all_filter_result.txt
for i in `ls %s/*xls`;do
awk -F'	' '{print $2"	"$(NF-1)"	"$NF}' $i;
done|sort|uniq|awk -F'	' 'NR==FNR{a[$1]=$0;next}{split($2,array,/:/);if (array[1] in a) print $1"	"a[array[1]];else if(array[2] in a)print $1"	"a[array[2]]}' - TF_protein_blast_all_filter.out >>TF_protein_all_filter_result.txt
%spython %s/module/Transcription_factor_correlation_analysis/TF_all_map.py
    z�
export PATH=/zfssz3/SP_MSI/Pipeline/software/application/pdftk:$PATH
export LD_LIBRARY_PATH=/zfssz3/SP_MSI/Pipeline/software/application/pdftk:$LD_LIBRARY_PATH
%spython %s/src/Submit_analysis_files_and_pdf_generation.py
sh ./deal.sh
sh %ssrc/pdf.sh

c             C   s�  | dkr�t dddd���}tt� tjd� x(tdd�D ]}td| � tjd� q6W tjj� jd	�}t	j
� jd
�dt }td||f � |jt� t	jdt � W d Q R X x6t	jjd�r�t	jdttf � t	jdttf � P q�W �n| dk�rxHd}x4tD ],}t	jjd| � r�t	jjd| � r�d}q�W |dkr�P q�W dtj� k�sTdtj� k�r`�xd}�x�tD �]�}t	jjd||f � �r�t	jjd||f � �r�d}t	jjd||f � �r�t	jjd||f � �r�d}t	jjd||f � �rt	jjd||f � �rd}t	jjd||f � �r<t	jjd||f �  �r<d}t	jjd||f � �rpt	jjd||f � �rpd}t	jjd||f � �r�t	jjd||f � �r�d}t	jjd||f � �r�t	jjd ||f � �r�d}t	jjd!||f � �rt	jjd"||f � �rd}|dk�rdt	jd#| � x�t	jd$�D ]v\}}}	xh|	D ]`}
d%|
k�rvd&|
k�rv|
jd%d'�}t	jd(|
|f � d)|
k�r@|
jd)d*�}t	jd(|
|f � �q@W �q0W t	jt� t	jd+| � xzt	jd$�D ]l\}}}	x^|	D ]V}
d'|
k�r
|
jd'd%�}t	jd(|
|f � d*|
k�r�|
jd*d)�}t	jd(|
|f � �q�W �q�W t	jt� �qdW |dk�rXP �qXW t d,ddd��R}tjj� jd	�}td-| � d.tj� k�r�|jt� dtj� k�r�|jt� W d Q R X x$t	jjd/��r�t	jd0t � P �q�W x6t	jjd1��r�t	jj d1��r�t	jd2t!tf � P �q�W x6t	jjd3��r&t	jj d3��r&t	jd4t!tf � P �q&W dtj� k�r�xdt	jjd5��rlt	jjd6��rlt	jj d5��rlt	jj d6��rlt	jd7t!tf � t	jd8t!tf � P �qlW d.t"j� k�r�x6t	jjd9��r�t	jj d9��r�t	jd:t!tf � P �q�W �n�| d;k�rt d<ddd���}x�t	jjd=��r�t	jj d=��r�tjj� jd	�}td>| � |jt#� |j$�  t	jjd?��r�t	jd@t � xTt	jjdA��r�t	jjdB��r�t	jj dC��r�t	jj dD��r�t	jdE� t	jdF� P �q�W P tjdG� �q6W W d Q R X �n�| dHk�rDt dIddd���}�xd}x<tD ]4}t	jjdJ| ��sXd}nt	jj dJ| ��s<d}�q<W |dk�r�d.t"j� k�r�t	jjdK��s�d}nt	jj dK��s�d}|dk�r2tjj� jd	�}tdL| � |jt%� |j$�  x t	jjdM��r�t	jdN� P �q�W x t	jjdO��rt	jdP� P �qW P �q2W W d Q R X �n�| dQk�	r6t dRddd���}x�d}xhtD ]`}t	jjdS| � �s�t	jjdT| � �r�d}n,t	jj dS| � �s�t	jj dT| � �rjd}�qjW |dk�r`tjj� jd	�}tdU| � |jt&� |j$�  t	jjdV��	r t	jdW� P P �q`W W d Q R X �n�| dXk�	r�t dYddd���}dtj� k�	r�x�t	jjdZ��	r`t	jjd[��	r`t	jj dZ��	r`t	jj d[��	r`tjj� jd	�}td\| � |jt'� |j$�  t	jjd]��	r�t	jd^t � P P �	q`W W d Q R X �n�| d_k�r�t d`ddd����}�x�d}x`tD ]X}t	jjda| ��
s@d}nt	jj da| ��
sVd}dtj� k�
r$t	jjdb| ��
s$d}�
q$W |dk�
rtjj� jd	�}tdc| � |jt(� |j$�  t	jjdd��
r�t	jde� t dfd�}d}x�tD ]�}|d7 }|jdgt � |jdh||f � |jdi||f � |jdj||f � |jdk||f � |jdl| � |jdm| � |jdn| � |dk�
r�|jdo| � |jdp| � |jdq| � |jdr| � �
q�W |j$�  x t	jjdf��r�t	jds� P �q�W P �
qW W d Q R X d S )uNr   zstep0.sh�wzUTF-8)�encoding�   �
   �   z%Y-%m-%d %H:%M:%Sr
   z'project_id:%s
starts time:%s,good luck!zHqsub -clear -cwd -l vf=0.5G,num_proc=1  -binding linear:1 -q %s step0.shz./submitz,%spython %s/src/Fasta_sequence_extraction.pyz5%spython %s/src/Function_Annotation_and_enrichment.pyz3./Data_Analysis/%s/Quantitative/transcription.fastaz-./Data_Analysis/%s/Quantitative/protein.fasta�yesz./%s/protein/%s_C.xlsz./%s/protein/%s_C.txtz./%s/protein/%s_F.xlsz./%s/protein/%s_F.txtz./%s/protein/%s_P.xlsz./%s/protein/%s_P.txtz./%s/protein/%s_path.xlsz./%s/protein/%s_path.txtz./%s/Transcription/%s_C.txtz./%s/Transcription/%s_C.xlsz./%s/Transcription/%s_F.txtz./%s/Transcription/%s_F.xlsz./%s/Transcription/%s_P.txtz./%s/Transcription/%s_P.xlsz./%s/Transcription/%s_path.txtz./%s/Transcription/%s_path.xlsz./%s/Transcriptionz./z.xlsZGeneDiffExpz.txtzmv %s %sz	_path.xlsz.pathz./%s/proteinzstep1.shzX##########step1:Blast and association analysis total file creation starts on %s#########�noz
./step1.shzHqsub -clear -cwd -l vf=0.5G,num_proc=1  -binding linear:1 -q %s step1.shz
./blast.shzHqsub -clear -cwd -l vf=%s,num_proc=3  -binding linear:3 -q %s ./blast.shz./blast_ppi.shzLqsub -clear -cwd -l vf=%s,num_proc=3  -binding linear:3 -q %s ./blast_ppi.shz./TF_protein_blast.shz./TF_transcription_blast.shzTqsub -clear -cwd -l vf=%s,num_proc=3  -binding linear:3 -q %s  ./TF_protein_blast.shzYqsub -clear -cwd -l vf=%s,num_proc=3  -binding linear:3 -q %s ./TF_transcription_blast.shz./ko_blast.shzLqsub -clear -cwd -l vf=%s,num_proc=5  -binding linear:5 -q %s  ./ko_blast.sh�   zstep2.shz./blast_all.outz9##########step2:Quantitative module starts on %s#########z
./step2.shzHqsub -clear -cwd -l vf=0.5G,num_proc=1  -binding linear:1 -q %s step2.shzQuantitative_volcano.shzQuantitative_heat.shz./Quantitative_volcano.shz./Quantitative_heat.shzsh Quantitative_volcano.shzsh Quantitative_heat.sh�<   �   zstep3.shz/./Data_Analysis/%s/Quantitative/Association.txtz ./all_transcription_ko.blast.outz5##########step3:Function module starts on %s#########z
./step3.shzsh step3.shzFunction_volcano.shzsh Function_volcano.shr   zstep4.shz&./Data_Analysis/%s/Function/all_CorMapz,./Data_Analysis/%s/Function/DEPs_DEGs_CorMapz4##########step4:Network module starts on %s#########z
./step4.shzsh step4.sh�   zstep5.shz ./TF_transcription_all_blast.outz./TF_protein_all_blast.outz/##########step5:TF module starts on %s#########z
./step5.shzHqsub -clear -cwd -l vf=0.5G,num_proc=1  -binding linear:1 -q %s step5.sh�   zstep6.shz*./Data_Analysis/%s/Network/ppi_network.pngz'./Data_Analysis/%s/TF/TF_violinplot.pngz0##########step6:PDF module starts on %s#########z
./step6.shzsh step6.shz	./deal.shzcp -r %s/lib/pdf ./submit
zTcp -r ./Data_Analysis/%s/Function/* ./submit/%s/Function_enrichment_analysis_result
z[cp -r ./Data_Analysis/%s/TF/* ./submit/%s/Transcription_factor_correlation_analysis_result
z]cp -r ./Data_Analysis/%s/Quantitative/* ./submit/%s/Quantitative_association_analysis_result
z_cp -r ./Data_Analysis/%s/Network/* ./submit/%s/Interaction_network_association_analysis_result
z$mv *.fasta ./submit/%s/Blast_result
z"mv *.out ./submit/%s/Blast_result
z"mv *.txt ./submit/%s/Blast_result
z:cp -r ./Data_Analysis/%s/Function/* ./submit/pdf/material
z4cp -r ./Data_Analysis/%s/TF/* ./submit/pdf/material
z>cp -r ./Data_Analysis/%s/Quantitative/* ./submit/pdf/material
z9cp -r ./Data_Analysis/%s/Network/* ./submit/pdf/material
z
sh deal.sh�����))�open�print�welcome�timeZsleep�range�datetime�now�strftime�os�getcwd�split�write�step0�popenr   �path�exists�system�python�home�array_group�whether_trans�lower�whether_pro�chdir�walk�replace�	home_root�TF�
step1_noTF�step1_TF�getsize�memory�KO�step2�close�step3�step4�step5�step6)r   Zwr0Zcourt�nowTimeZ
project_idZisrun1�index�parentZdirnames�	filenames�name�new_nameZwr1Zwr2Zwr3Zisrun3Zwr4Zisrun4Zwr5Zwr6Zisrun6�wrZgroup_index� rG   �4/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/main.py�runm   s�   




$00020000























((


















rI   �__main__�-r   r   z(./submit/correlation_analysis_report.pdfzrm ./deal.shZBGI�   � �   g�������?r   g�������?r   � z%Y-%m-%d %H:%M:%Sz)Successful,Congratulations!Completed on%s�
i����r   i����)Ar!   Zjsonr   r   r"   r3   r   Zmyfile�load�result�groupr+   r   r   r   r8   r*   Znetwork_memoryr9   r4   r   r   r   r-   r/   r#   r,   �userr.   ZTF_databaser   r%   r6   r5   r:   r<   r=   rA   r>   r?   rI   �__name__Zsmile�intZarrayr   �ir'   r(   r)   Zsentence�charZallChar�yZlstZlst_con�xZformula�len�appendr   r    r@   r   �joinrG   rG   rG   rH   �<module>   s�   


	(
	  





$


8

