3
�|N\�  �            J   @   s�  d dl Z d dlZd dlZedk�r�edd�Ze je�Zed d Zed d Z	e	j
d�Zi Zed	e ��>Zx6ej� D ]*Zej� Zej
d
�Zed eded   < qtW W dQ R X �x�eD �]�Zi Zi Zi Zde Zi Zi Zded< ded< i Zi Zi Zedeef ��tZd Zxhej� D ]\Zed k�r,ed7 Z�qej� Zej
d
�Zed eed  < eed �dk�rdeed  < �qW W dQ R X edeef ��tZd Zxhej� D ]\Zed k�r�ed7 Z�q�ej� Zej
d
�Zed eed  < eed �dk�r�deed  < �q�W W dQ R X edeef ���Zd Zx�ej� D ]�Zej� Zej
d
�Zed k�r�xHeee��D ]8Z ee  dk�rje Z!dee  k�rTdee  k�rTe Z"�qTW ed7 Z�q&dee" j#� k�s�dee" j#� k�r&eee"  eee! < �q&W W dQ R X i Z$edeef ��|Zd Zxpej� D ]dZej� Zej
d
�Zed k�r^x(eee��D ]Z ee  dk�r6e Z!�q6W ed7 Z�qde$ee! < �qW W dQ R X edeef ��|Zd Zxpej� D ]dZej� Zej
d
�Zed k�r�x(eee��D ]Z ee  dk�r�e Z!�q�W ed7 Z�q�de$ee! < �q�W W dQ R X ede ��fZd ZxZej� D ]NZed k�rBed7 Z�q(ej� Zej
d
�Zed eed  < ed eed < �q(W W dQ R X ede d �Z%ed!e d���"Zd Z&ej'd"�Z(�x
ej� D ]�Zej� Zej
d
�Zd#ed  k�rTej)e(d$ed  �ed < ed  j*d#d$�Z+e+ej,� k�r6e&d7 Z&e%j-d%e+ee+ f � ne&d7 Z&e%j-d&e+e$e+ f � d'ed  k�r�ej)e(d$ed  �ed < ed  j*d'd$�Z+e+ej,� k�r��q�ne&d7 Z&e%j-d(e+ee+ f � �q�W W dQ R X ed)e d �Z%ed*e d����Zd Z�x�ej� D �]�Zej� Zej
d
�Zed k�rZed7 Zd+e& ed< e%j-d,ed  ed ed ed f � �q�ed j
d-�Z.g Z/x~e.D ]vZ d#e k�r�e j*d#d$�Z+ej)d"d$e+�Z+e/j0e+� d'e k�rre j*d'd$�Z+ej)d"d$e+�Z+e+ej,� k�rܐqrn
e/j0e+� �qrW ed  ej,� k�r�ee/�d k�r�ed  ek�r d.Z1need   Z1ed  ek�r@d.Z2need   Z2e%j-d/ed  ee/�ed eed  d-j3e/�e1e2f � �q�W W dQ R X q�W dS )0�    N�__main__zcorrelation_config.json�rZBasis_Informationz(Correlation analysis process server pathZComparison_Group�,z%slib/map_title.tab�	�   zko%sz ./Data_Analysis/%s/Quantitative/ZDownZUpz./%s/protein/%s_path.xls�   �   g�������?z./%s/Transcription/%s_path.txtz%./%s/Transcription/%s.GeneDiffExp.xlsZGeneIDZupZdownz./%s/protein/%s_Up.xlsZ
Protein_IDz./%s/protein/%s_Down.xlsz%sAssociation.txt�   �   z(./Data_Analysis/%s/Network/network.glist�wz1./Data_Analysis/%s/Function/glist/DEPs_DEGs.glistz\(.*\)Z_Protein� z%s	%s	correlation
z%s	%s	uniq_protein
Z_mRNAz%s	%s	uniq_transcription
z'./Data_Analysis/%s/Network/network.pathz;./Data_Analysis/%s/Function/DEPs_DEGs_CorMap/DEPs_DEGs.pathz	Count(%s)z.%s	%s	%s	level_1	%s	trans_p_value	pro_p_value
�;ZNAz%s	%s	%s	%s	%s	%s	%s
)4Zjson�os�re�__name__�openZmyfile�load�result�home�group�splitZarray_groupZkoZfh�	readlines�line�stripZarray�indexZproZtransZcorrelation�rootZ	trans_allZratio�pathZpro_pZtrans_p�n�float�range�len�iZIdZ
Regulation�lowerZpro_all�wr�u�compileZpattern�sub�replace�name�keys�writeZsequence_array�new�append�a�b�join� r0   r0   �M/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/Network_process_file_creation.py�<module>   s2  




"






$$







 

&

&



