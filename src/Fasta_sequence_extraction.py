3
4?\DF  �            	   @   sH  d dl Z d dlZd dlmZ d dlZG dd� d�Zedk�rDedd�Ze j	e�Z
e
d d	 Ze
d d
 Ze
d d Ze
d d Zee�Ze
d d Zee�Zee�Ze
d d Ze
d d Zejd�Ze� Z�xtejjd�rАx^eD �]TZx�ejde �D ]�\ZZZdZdZdZxDeD ]<Z de e k�r,e Zde e k�r>e Zde e k�re Z�qW edkr�edkr�edkr�ej!deef deef deef eee� q�W x�ejde �D ]�\ZZZdZ"dZ#x2eD ]*Z de e k�r�e Z"de e k�r�e Z#�q�W e"dk�se#dk�re$d� n"ej%dee"f dee#f eee� �q�W q�W P q�W dS )�    N)�SeqIOc               @   s   e Zd Zdd� Zdd� ZdS )�extract_fastac          	   C   s@  |d }g }t d| d�}	d}
d}d}d}d}d }d!}t |d�}�x |j� D �]}|j� }|jd�}|dk�r�x�tt|��D ]~}|| dkr�|}|| d	kr�|}d
|| kr�|}nd|| kr�|d"kr�|}d|| kr�|}d|| kr�|}|| dkr||}q|W |d7 }|d#k�rtd� d}
|d$k�r2td� d}
|d%k�rHd}
td� |d&k�r^d}
td� |d'k�rtd}
td� |
dkrLtd� P qLd|| k�r�|| jd�}d|k�r�|jd�}|d k�r�t|�||< t	|| �|k�r�|||< n|||< || dkrL|| dkrL|| dkrLt	|| �}|j
|| � |	jd|| || tj|d�|| || f � qLW d}t |d�}�x>|j� D �]0}|j� }|jd�}|dk�r�x�tt|��D ]�}|| dk�r�|}|| d	k�r�|}d
|| k�r�|}nd|| k�r|d(k�r|}d|| k�r|}d|| k�r*|}|| dk�r�|}�q�W |d7 }|d)k�r`td� d}
|d*k�rvtd� d}
|d+k�r�d}
td� |d,k�r�d}
td� |d-k�r�d}
td� |
dk�r~td� P �q~|j
|| � d|| k�rH|| jd�}d|k�r|jd�}|d k�r@t|�||< t	|| �|k�rH|||< n|||< || dk�r~|| dk�r~|| dk�r~t	|| �}|	jd|| || tj|d�|| || f � �q~W d}t |d�}�xv|j� D �]h}|j� }|jd�}|dk�r x�tt|��D ]�}|| dk�r|}|| d	k�r&|}d
|| k�r:|}nd|| k�rV|d.k�rV|}d|| k�rh|}d|| k�rz|}|| dk�r�|}�q�W |d7 }|d/k�r�td� d}
|d0k�r�td� d}
|d1k�r�d}
td� |d2k�r�d}
td� |d3k�rd}
td� |
dk�r�td� P �q�|| |k�r�d|| k�r�|| jd�}d|k�r^|jd�}|d k�rvt|�||< n|d ||< || dk�r�|| dk�r�|| dk�r�|| dk�r�t	|| �}t	|| �|k �r�||k�s�|d| k �r�|d ||< |dk�r�|	jd|| || tj|d�|| || f � �q�W d S )4Ng{�G�z�?z-./Data_Analysis/%s/Quantitative/protein.fasta�wr   �   �r�	Z
Protein_ID�DescriptionZMean_Ratio_ZRatio_ZPvalue_ZQvalue_ZProtein_SequencezRerror:protein of title id is not found!Please modify your protein id as Protein_IDzderror:protein of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]zeerror:protein of title Description is not found!Please modify your protein Description as Descriptionzxerror:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]zderror:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequencez*Please correct the error before proceeding�|�-ZNAz>%s %s-<%s-<%s-<Down
%s
�   z>%s %s-<%s-<%s-<Up
%s
zn/az>%s %s-<%s-<%s-<None
%s
�����r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   )�open�	readlines�strip�split�range�len�print�remove�min�float�append�write�math�log�max)�selfZprotein_xls_fileZupZdown�name�	protein_p�protein_foldZ	ThresholdZisupdown�wr�error�n�IdZPvaluer   �Ratio�Sequence�fh�line�array�iZp_value_array�ratio� r+   �I/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Fasta_sequence_extraction.py�protein_deal
   sl   











$.













*6












8
zextract_fasta.protein_dealc             C   sZ  i }d|d< d|d< d|d< d|d< t |d�}t d| d�}i }	i }
d|j� kr�tjjd	| �r�t d	| d��:}x2|j� D ]&}|j� }|jd
�}|d |
|d < qzW W d Q R X ntd� d S n�d|j� k�rZt d	| d�}t |d��h}d}x\|j� D ]P}|j� jd
�}|dk�r|d7 }q�|j	d|d |d f � |d |
|d < q�W W d Q R X |j
�  x&tj|d�D ]}t|j�|	|j< �qhW d}d}d$}d%}d&}d'}d(}�x�|j� D �]�}|j� }|jd
�}|dk�r�x~tt|��D ]n}|| dk�r�|}d|| k�r|}d|| k�r|}d|| k�r4d|| k�r4|}d|| k�r�|}�q�W |d7 }|d)k�rjd}td� |d*k�r�d}td� |d+k�r�td� |d,k�r�td� |d-k�r�d}td� |dk�r�td� P �q�|| |k�r�|| |
j� k�rP|
||  |	k�rPd|| j� k�rP|d.k�r�|d/k�r`|j	d|| || || || |	|
||   f � n.|j	d|| || || |	|
||   f � nb|d0k�r�|j	d|| || || |	|
||   f � n(|j	d|| || |	|
||   f � �q�|| |
j� k�r�|
||  |	k�r�d|| j� k�r�|d1k�r�|d2k�r�|j	d || || d3t|| � || |||  |	|
||   f � n@|j	d!|| || d4t|| � |||  |	|
||   f � n�|d5k�r|j	d"|| d6t|| � || |||  |	|
||   f � n:|j	d#|| d7t|| � |||  |	|
||   f � �q�W d S )8NZDownZUp�*r
   r   z3./Data_Analysis/%s/Quantitative/transcription.fastar   Zgenez./%s/Transcription/gene2trr   r   r   zAPlease put the corresponding gene2tr file in the desired locationZmrnaz%s	%s
ZfastaZGeneIDr   Zlog2�valuezVerror:transcription of title id is not found!Please modify your transcription id as Idzverror:transcription of title Regulation is not found!Please modify your transcription Regulation as Up-Down-Regulationzewarning:transcription of title pvalue is not found!Please modify your transcription pvalue as p-valuezswarning:transcription of title Description is not found!Please modify your transcription Description as Descriptionz�error:transcription of title Mean Ratio is not found!Please modify your transcription Mean Ratio as Mean_Ratio_[sample of your name]z*Please correct the error before proceedingZnaz>%s %s-<%s-<%s-<None
%s
z>%s %s-<%s-<None-<None
%s
z>%s None-<%s-<%s-<None
%s
z>%s None-<%s-<None-<None
%s
z>%s %s-<%s-<%s-<%s
%s
z>%s %s-<%s-None-<%s
%s
z>%s None-<%s-<%s-<%s
%s
z>%s None-<%s-<None-<%s
%s
r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   )r   �lower�os�path�existsr   r   r   r   r   �closer   Zparse�str�seq�idr   r   �keysr   )r   Ztrans_xls_fileZtrans_sequence_filer   �type�trans_nodiffr*   r&   r    Z	trans_seqZRNA_IDZuhr'   r(   ZwtZftr"   Z
seq_recordr!   r#   Zpvaluer   r$   Z
Regulationr)   r+   r+   r,   �transcription_deal�   s�    

 














B"
"z extract_fasta.transcription_dealN)�__name__�
__module__�__qualname__r-   r;   r+   r+   r+   r,   r   	   s    gr   �__main__zcorrelation_config.jsonr   ZBasis_InformationZComparison_GroupzTranscriptome ID typezFilter ParameterszProtein p value ThresholdZProteinFoldChangezGene p value ThresholdzGene Non-difference label�Reference_data_set�,z./Data_Analysisz./%s/protein� z%s.xlsz	%s_Up.xlsz%s_Down.xlsz./%s/protein/%sz./%s/Transcriptionz%s.GeneDiffExp.xlsz%sz;error:Missing transcript file, please check transcript filez./%s/Transcription/%s)&Zjsonr1   ZBior   r   r   r<   r   Zmyfile�load�result�groupr9   r   r   r   Zgene_pr:   r@   r   Zarray_group�Qr2   r3   �index�walk�parentZdirnames�	filenamesZall_xlsZup_xlsZdown_xlsr   r-   Zfile1Zfile2r   r;   r+   r+   r+   r,   �<module>   sb     x





0


,