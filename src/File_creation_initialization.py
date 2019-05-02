3
�\g  �               @   s�  d dl Z d dlZd dlZdd� Zdd� Zedk�r�ej� Zedd�Z	e j
e	�Zed	 d
 Zed	 d Zed	 d Zed	 d Zed	 d Zejd�Z�xheD �]^Zee� �xNejjde �o�ejjde �r�eje� ejdeeef � ejdeeef � ejdeef � eje� ejdeef � x�ejd�D ]�\ZZZx�eD ]�Zdek�r�dek�r�ejdd�Zejdeef � dek�r�ejdd�Zejdeef � dek�r�ejdd�Zejdeef � dek�r�ejdd�Zejdeef � dek�rJejdd�Zejdeef � �qJW �q:W eje� eje� ejd eeef � eje� ejd!eef � xzejd�D ]l\ZZZx^eD ]VZdek�r�ejdd�Zejdeef � dek�r�ejdd�Zejdeef � �q�W �q|W eje� P q�W q�W ejjd"��re d#� n
ejd$� ejjd%��r:e d&� n
ejd'� �xejjd%��rHe d(� ejd%� x�eD ]�Zejjd)e ��s�ejd*e � x�ejjd)e ��r�ejd)e � ejjd+��s�ejd,� ejjd-��s�ejd.� ejjd/��s�ejd0� ejjd1��sejd2� ejjd3��s,ejd4� P �q�W ejd5e � �qnW eje� P �qHW x.ejjd"��r\xeD ]Zee� �qpW P �q\W dS )6�    Nc             C   s�   t jjd|  �st jd|  � x�t jjd|  �r t jjd|  �sNt jd|  � t jjd|  �slt jd|  � t jjd|  �s�t jd|  � t jjd	|  �s�t jd
|  � P q W d S )Nz./Data_Analysis/%szmkdir ./Data_Analysis/%sz./Data_Analysis/%s/Quantitativez%mkdir ./Data_Analysis/%s/Quantitativez./Data_Analysis/%s/Functionz!mkdir ./Data_Analysis/%s/Functionz./Data_Analysis/%s/TFzmkdir ./Data_Analysis/%s/TFz./Data_Analysis/%s/Networkz mkdir ./Data_Analysis/%s/Network)�os�path�exists�popen)�name� r   �L/ldfssz1/SP_MSI/Pipeline/Pipeline/TP_Cor/src/File_creation_initialization.py�make_analysis_file   s    r	   c             C   sr   t jjd|  �st jd|  � xNt jj| �r t jjd|  �sJt jd|  � t jjd|  �sht jd|  � P q W d S )Nz%szmkdir %sz./%s/Transcriptionzmkdir ./%s/Transcriptionz./%s/proteinzmkdir ./%s/protein)r   r   r   r   )r   r   r   r   �make_input_file   s    r
   �__main__zcorrelation_config.json�rZBasis_InformationZComparison_Groupz(Correlation analysis process server path�Reference_data_set�Transcriptome_path�Proteomics_path�,z./%s/Transcriptionz./%s/proteinzcp ./%s* %s/%s/Transcriptionzcp ./%s %s/%s/Transcriptionzcp gene2tr %s/%s/Transcriptionz%s/%s/Transcriptionz./z.xlsZGeneDiffExpz.txtzmv %s %sz	_path.xlsz.pathz	_path.txtz	.path.xlsz	.path.txtzcp ./%s* %s/%s/proteinz%s/%s/proteinz./Data_Analysisz^warning:Data_Analysis is existed in your root directory, please make sure the folder is empty!zmkdir Data_Analysisz./submitzXwarning:sublmit is existed in your root directory, please make sure the folder is empty!zmkdir submitz$Initializing, please wait...........z./%sz
mkdir ./%sz./Blast_resultzmkdir ./Blast_resultz1./Interaction_network_association_analysis_resultz7mkdir ./Interaction_network_association_analysis_resultz*./Quantitative_association_analysis_resultz0mkdir ./Quantitative_association_analysis_resultz2./Transcription_factor_correlation_analysis_resultz8mkdir ./Transcription_factor_correlation_analysis_resultz%./Function_enrichment_analysis_resultz+mkdir ./Function_enrichment_analysis_resultz	%s/submit)!Zjsonr   Zos.pathr	   r
   �__name__�getcwd�root�openZmyfile�load�result�group�homer   r   r   �splitZarray_group�indexr   r   �chdirr   �walk�parentZdirnames�	filenamesr   �replace�new_name�system�printr   r   r   r   �<module>   s�   




 



























