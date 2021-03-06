3
�\�  �               @   s  d dl Z d dlZd dlmZ edk�re j� Zedd�Zej	e�Z
e
d d Zejd�Z�x�e jjd	�r\�x�eD �]�Zi Zi ZxDejd
e d�D ]0Zeej�jd�Zed ed ed geej< q�W xDejde d�D ]0Zeej�jd�Zed ed ed geej< q�W ede d�Zejd� edd���Zx�ej� D ]�Zej� Zejd�Zed  ej� k�r8ed ej� k�r8ejded  ed e eed   d  �eed   d eed   d e eed  d  �eed  d eed  d f � �q8W W dQ R X qpW P q\W dS )�    N)�SeqIO�__main__zcorrelation_config.json�rZBasis_InformationZComparison_Group�,z./Data_Analysisz-./Data_Analysis/%s/Quantitative/protein.fastaZfastaz-<�   �   �   z3./Data_Analysis/%s/Quantitative/transcription.fastaz/./Data_Analysis/%s/Quantitative/Association.txt�wzuprotein_ID	gene_ID	protein_log2FC	protein_FDR	protein_type	transcription_log2FC	transcription_FDR	transcription_type
z./blast_all_filter.out�	z%s	%s	%.3f	%s	%s	%.3f	%s	%s
)!�osZjsonZBior   �__name__�getcwd�pwd�openZmyfile�load�result�group�splitZarray_group�path�exists�indexZproteinZtranscriptionZparseZ
seq_record�strZdescriptionZarray�id�wr�writeZfh�	readlines�line�strip�keys�float� r    r    �P/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Associated_total_file_generation.py�<module>   s8   



  

$�