3
��\�'  �            ,   @   s�  d dl Z d dlZdd� Zedk�r�edd�Zeje�Zed d Zed d	 Z	ed
 d Z
ed
 d Zejd�Z�x.eD �]$Zde Zde Zdeef Zi Zi Zedeef ��PZd ZxDej� D ]8Zed kr�ed7 Zq�ej� Zejd�Zed eed  < q�W W dQ R X edeef ��VZd ZxJej� D ]>Zed k�rBed7 Z�q(ej� Zejd�Zed eed  < �q(W W dQ R X �x&e jjdeef ��rxe jjdeef ��rxd>Zd?Zd@ZdAZ dBZ!d Zd Z"ede d�Z#edeef d����Z�x�ej� D �]�Zej� Zejd�Zed k�rTx�e$e%e��D ]�Z&ee& dk�r6e&Zee& dk�rHe&Zdee& k�r\e&Z ndee& k�rxe dCk�rxe&Z dee& k�r�e&Zdee& k�r�e&Zee& dk�r�e&Z!d ee& k�r e&Z'�q W edDk�r�e(d!� dZ"edEk�r�e(d"� dZ"edFk�rdZ"e(d#� e dGk�rdZ"e(d$� e!dHk�r4dZ"e(d%� e"dk�rHe(d&� P ed7 Z�q�eee  ��r�e#j)d'ee ee  ee' f � �q�W W dQ R X i Z*dIZdJZ+dKZdLZ dMZ,dNZ!d Zd Z"ed(eef d���^Z�xTej� D �]FZej� Zejd�Zed k�r x~e$e%e��D ]nZ&ee& d)k�re&Zdee& k�r0e&Zd*ee& k�rBe&Z d+ee& k�rbd,ee& k�rbe&Z,d-ee& k�re&Z+�qW ed7 ZedOk�r�dZ"e(d.� e,dPk�r�dZ"e(d/� e+dQk�r�e(d0� edRk�r�e(d1� e dSk�r�dZ"e(d2� e"dk�r�e(d&� P �q�eee  ��r�ee  e*ee < �q�W W dQ R X �xde jje��r2ed3e d�Z#eed���Zd Zx�ej� D ]�Zd4ek�rz�qhej� Zejd�Ze%e�dk�r�ed  j-d5d6�e*j.� k�r"e#j)d7ed  e*ed  j-d5d6� f � nFed  j-d5d6�e*j.� k�rhe#j)d8ed  e*ed  j-d5d6� ed f � �qhW W dQ R X e#j/�  e jjd9e ��rVe(d:� ne j0d;e � e(d:� e j0d<e � e j0d=eeef � P �q2W P �qxW qxW dS )T�    Nc             C   sV   yt | � dS  tk
r    Y nX ydd l}|j| � dS  ttfk
rP   Y nX dS )NTr   F)�float�
ValueError�unicodedataZnumeric�	TypeError)�sr   � r   �K/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/mRNA_and_protein_ko_combine.py�	is_number   s    
r	   �__main__zcorrelation_config.json�rZBasis_InformationZComparison_Group�R_HOME_PATHZ
AnnotationZNR_Species_typez'Whether the transcriptome ko file exist�,z./Data_Analysis/%s/Function/z3./Data_Analysis/%s/Quantitative/transcription.fastaz./%s/Transcription/%s.koz%s/protein/%s_path.xls�   �	�   z%s/Transcription/%s_path.txtz%sprotein.ko�wz./%s/protein/%s.xlsZ
Protein_ID�DescriptionZMean_Ratio_ZRatio_ZPvalue_ZQvalue_ZProtein_Sequence�KEGGzXerror:transcription of title id is not found!Please modify your protein id as Protein_IDzjerror:transcription of title Pvalue is not found!Please modify your protein Pvalue as Pvalue_[sample_name]zeerror:protein of title Description is not found!Please modify your protein Description as Descriptionzxerror:protein of title Mean Ratio is not found!Please modify your protein Mean Ratio as Mean_Ratio_[sample of your name]zderror:protein of title Sequence is not found!Please modify your protein Sequence as Protein_Sequencez*Please correct the error before proceedingz%s_Protein(%s)	%s
z%./%s/Transcription/%s.GeneDiffExp.xlsZGeneIDZlog2ZUpZDown�valuezVerror:transcription of title id is not found!Please modify your transcription id as Idzverror:transcription of title Regulation is not found!Please modify your transcription Regulation as Up-Down-Regulationzewarning:transcription of title pvalue is not found!Please modify your transcription pvalue as p-valuezswarning:transcription of title Description is not found!Please modify your transcription Description as Descriptionz�error:transcription of title Mean Ratio is not found!Please modify your transcription Mean Ratio as Mean_Ratio_[sample of your name]z	%smRNA.ko�#Z_mRNA� z%s(%s)
z
%s(%s)	%s
z%sglistzAKEGG pathway is finished!Integrating analysis is on the way......zmkdir %sglistzsed -i '/#/d' %smRNA.koz(cat %sprotein.ko %smRNA.ko>%spro_mRNA.ko�����r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   r   )1�osZjsonr	   �__name__�openZmyfile�load�result�groupr   ZSpeciesZko�splitZarray_group�index�rootZtransZoutput_transZpro_pZtrans_pZfh�n�	readlines�line�stripZarray�path�exists�getsizeZIdZPvaluer   ZRatio�Sequence�error�wr�range�len�ir   �print�writeZtrans_expression_dicZpvalueZ
Regulation�replace�keys�close�popenr   r   r   r   �<module>   sP  






 








0








 

(<
