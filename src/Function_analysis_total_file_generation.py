3
�rN\�"  �               @   s�  d dl Z d dlZdd� Zdd� Zedk�r�edd�Zeje�Zed	 d
 Z	ed	 d Z
e	jd�Z�xte jjd�rd�x^eD �]TZde Zi Zede d��PZd ZxDej� D ]8Zed kr�ed7 Zq�ej� Zejd�Zed  eed < q�W W dQ R X deef Zdeef Zdeef Zdeef Zdeef Zdeef Zdeef Zdeef Zde Z de Z!de Z"de Z#de Z$de Z%d e Z&d!e Z'eeee e$e� eeee!e%e� eeee"e&e� eeee#e'e� qxW P qdW dS )"�    Nc             C   sV  t |d�}t |d�}|jd� |jd� i }i }t | d��^}	d}
xR|	j� D ]F}|j� }|jd�}|
dkr�|
d7 }
|d jd�d	kr�qJ|||d < qJW W d Q R X t |d��^}	d}
xR|	j� D ]F}|j� }|jd�}|
dkr�|
d7 }
|d jd�d	kr�q�|||d < q�W W d Q R X �xB|j� D �]4}g }||j� k�r|| jd�}|| jd�}|d
 jd�}|d
 jd�}g }x>|D ]6}|jd�d |j� k�rr|j||jd�d  � �qrW x"|D ]}||k�r�|j|� �q�W t|d �dk �rt|d �dk �r|jdt|d �t|d �f � njt|d �dk�r`t|d �dk�r`|jdt|d �t|d �f � n"|jdt|d �t|d �f � t|d �dk �s�t|d �dk �rt|d jd�d �t|d jd�d � }t|d jd�d �t|d jd�d � }|jd||d jd�d |d jd�d t	|�|d |d dj
|�||f	 � �qW d S )N�wz3protein_P_value	transcription_P_value	significance
z�GO_Term	protein_num	tanscription_num	correlation_num	protein_P_value	transcription_P_value	correlation_proteinID_array	protein_Enrichment_factor	transcription_Enrichment_factor
�rr   �	�   zGO:F�   �,�(�   g�������?z%.3f	%.3f	Both_of_Significance
z%.3f	%.3f	None_of_Significance
z!%.3f	%.3f	Either_of_Significance
�   � �   z%s	%s	%s	%s	%s	%s	%s	%s	%s
)�open�write�	readlines�strip�split�
startswith�keys�append�float�len�join)�	input_pro�input_trans�output1�output2�correlation_id�wr1�wr2�protein�transcription�fh�n�line�array�id�correlation_function�	pro_array�trans_array�pro_id_array�trans_id_array�pro_id_trans�index�pro_Enrichment_factor�trans_Enrichment_factor� r/   �W/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Function_analysis_total_file_generation.py�GO_file_deal   sj    







$$$,,r1   c             C   s\  t |d�}t |d�}|jd� |jd� i }i }t | d���}	d}
x�|	j� D ]�}|j� }|jd�}|
dkr�x4tt|��D ]$}|| dkr�|}|| dkrv|}qvW |
d	7 }
|
d	7 }
|d jd
�dkr�qJ|||d < qJW W d Q R X t |d��b}	d}
xV|	j� D ]J}|j� }|jd�}|
dk�r4|
d	7 }
|d jd
�dk�r4q�|||d < q�W W d Q R X �x|j� D �]�}g }||j� k�rZ|| jd�}|| jd�}|| jd�}|| jd�}g }x>|D ]6}|jd�d |j� k�r�|j	||jd�d  � �q�W x"|D ]}||k�r�|j	|� �q�W t
|d �dk �rZt
|d �dk �rZ|jdt
|d �t
|d �f � njt
|d �dk�r�t
|d �dk�r�|jdt
|d �t
|d �f � n"|jdt
|d �t
|d �f � t
|d �dk �s�t
|d �dk �rZt
|d	 �t
|d � }t
|d	 �t
|d � }|jd||d	 |d	 t|�|d |d dj|�||f	 � �qZW d S )Nr   z3protein_P_value	transcription_P_value	significance
z�Pathway	protein_num	tanscription_num	correlation_num	protein_P_value	transcription_P_value	correlation_proteinID_array	protein_Enrichment_factor	transcription_Enrichment_factor
r   r   r   �Proteins�KOsr   z#PathwayTr   r   r   g�������?z%.3f	%.3f	Both_of_Significance
z%.3f	%.3f	None_of_Significance
z!%.3f	%.3f	Either_of_Significance
r
   z%s	%s	%s	%s	%s	%s	%s	%s	%s
)r   r   r   r   r   �ranger   r   r   r   r   r   )r   r   r   r   r   r   r   r   r    r!   r"   r#   r$   �ir2   r3   r%   r&   r'   r(   r)   r*   r+   r,   r-   r.   r/   r/   r0   �Pathway_file_dealB   sv    








$$$r6   �__main__zcorrelation_config.jsonr   ZBasis_InformationZComparison_Group�R_HOME_PATHr   z./Data_Analysisz ./Data_Analysis/%s/Quantitative/z%sAssociation.txtr   r   z./%s/protein/%s_C.xlsz./%s/protein/%s_F.xlsz./%s/protein/%s_P.xlsz./%s/protein/%s_path.xlsz./%s/Transcription/%s_C.txtz./%s/Transcription/%s_F.txtz./%s/Transcription/%s_P.txtz./%s/Transcription/%s_path.txtz(./Data_Analysis/%s/Function/GO_C_all.txtz(./Data_Analysis/%s/Function/GO_F_all.txtz(./Data_Analysis/%s/Function/GO_P_all.txtz+./Data_Analysis/%s/Function/Pathway_all.txtz$./Data_Analysis/%s/Function/GO_C.txtz$./Data_Analysis/%s/Function/GO_F.txtz$./Data_Analysis/%s/Function/GO_P.txtz'./Data_Analysis/%s/Function/Pathway.txt)(�osZjsonr1   r6   �__name__r   Zmyfile�load�result�groupr8   r   Zarray_group�path�existsr,   �rootr   r!   r"   r   r#   r   r$   Zinput_pro_cZinput_pro_fZinput_pro_pZinput_pro_pathZinput_trans_cZinput_trans_fZinput_trans_pZinput_trans_pathZ	output_c1Z	output_f1Z	output_p1Zoutput_path1Z	output_c2Z	output_f2Z	output_p2Zoutput_path2r/   r/   r/   r0   �<module>   sX   <C




