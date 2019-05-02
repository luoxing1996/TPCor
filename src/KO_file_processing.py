3
_��\�  �               @   s\  d dl Z d dlZedk�rXe j� Zedd�Zeje�Zed d Z	ed d Z
ed d	 Zed d
 Zed d Zed d Ze	jd�Zx�eD ]�Zde Zde Zdeef Zi Zi Zdej� kr�dej� kr�e jjdeef �s�ede � q�q�e je� edd�Zejdeeeef � ej�  x.e jjd��r&e jde
 � e je� P �q&W q�W dS )�    N�__main__zcorrelation_config.json�rZBasis_InformationZComparison_Group�SGEQueueZ
AnnotationZNR_Species_typeZ	root_KEGGz5Whether to do transcriptome annotation and enrichmentz'Whether the transcriptome ko file exist�,z./Data_Analysis/%s/Function/z3./Data_Analysis/%s/Quantitative/transcription.fastaz./%s/Transcription/%s.ko�no�yesz�%s:Unable to find the ko file of the transcript group. If there is no ko file, set Whether the transcriptome ko file exist to no.zko.sh�wz�perl  /zfssz3/SP_MSI/Pipeline/FuctionalAnalysis/subroutine/blast2ko_v81.pl -input ../Data_Analysis/%s/Quantitative/transcription.fasta -kegg %s/%s.fa -blastout ../all_transcription_ko.blast.out -type blastout  -output ./Transcription/%s.kozEqsub -clear -cwd -l vf=0.5G,num_proc=1  -binding linear:1 -q %s ko.sh)�osZjson�__name__�getcwd�path�openZmyfile�load�result�groupr   ZSpeciesZKEGGZwhether_transZko�splitZarray_group�index�rootZtransZoutput_transZpro_pZtrans_p�lower�exists�print�chdir�wr�write�close�system� r   r   �B/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/KO_file_processing.py�<module>   sF   








